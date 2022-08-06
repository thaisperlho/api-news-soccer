from fastapi import FastAPI

from app.resource import news

app = FastAPI(title="Rest API", description="Thais Carvalho")

news.init_app(app=app)
