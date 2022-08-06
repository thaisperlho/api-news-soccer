from fastapi import FastAPI

from app.resource import news

app = FastAPI()

news.init_app(app=app)
