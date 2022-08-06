from datetime import datetime
from typing import List

import sqlalchemy
from app.config.settings import Settings
from app.schema.common.news import ModelNews

metadata = sqlalchemy.MetaData()

table = sqlalchemy.Table(
    "news",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("title", sqlalchemy.VARCHAR),
    sqlalchemy.Column("description", sqlalchemy.VARCHAR),
    sqlalchemy.Column("image", sqlalchemy.VARCHAR),
    sqlalchemy.Column("link", sqlalchemy.VARCHAR),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now),
    sqlalchemy.Column(
        "updated_at", sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now
    ),
)


class News:
    def __init__(self) -> None:
        self.table = table
        self.model = ModelNews
        self.engine = sqlalchemy.create_engine(Settings.db_uri)
        self.conn = self.engine.connect()
        self.conn.execution_options(isolation_level="AUTOCOMMIT", autocommit=True)

        metadata.create_all(self.conn)

    def __del__(self) -> None:
        self.conn.close()

    def get(self) -> List[ModelNews]:
        sql = self.table.select()
        rows = self.conn.execute(sql).all()
        return [self.model.from_orm(row) for row in rows]

    def get_by_id(self, id: int) -> ModelNews:
        sql = self.table.select().where(self.table.c.id == id)
        row = self.conn.execute(sql).first()
        return self.model.from_orm(row) if row else None

    def add(self, data: ModelNews) -> ModelNews:
        sql = self.table.insert().values(**data.dict(exclude_none=True))
        row = self.conn.execute(sql)
        return self.get_by_id(id=row.inserted_primary_key.id)

    def change(self, data: ModelNews, id: int) -> ModelNews:
        sql = (
            self.table.update()
            .where(self.table.c.id == id)
            .values(**data.dict(exclude_none=True))
        )
        self.conn.execute(sql)
        return self.get_by_id(id=id)

    def delete(self, id: int) -> ModelNews:
        row = self.get_by_id(id=id)
        sql = self.table.delete().where(self.table.c.id == id)
        self.conn.execute(sql)
        return row
