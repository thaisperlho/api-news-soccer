from audioop import add
from datetime import datetime
from unittest import result

from sqlmodel import Field, SQLModel, Session, create_engine, select

class Items(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

item_1 = Items(name="Teste1", price=600, is_offer= True)
item_2 = Items(name="Teste2", price=600, is_offer= True)
item_3 = Items(name="Teste3", price=600, is_offer= True)
item_4 = Items(name="Teste4", price=600, is_offer= True)

conn = create_engine("postgresql://postgres:1234@localhost:5432/postgres", echo=False)

SQLModel.metadata.create_all(conn)

#with Session(conn) as session:
#    session.add(item_1)
#    session.add(item_2)
#    session.add(item_3)
#    session.add(item_4)
#    session.commit()

with Session(conn) as session:
    sql = select(Items)
    result = session.exec(sql).all()
    print(result)


