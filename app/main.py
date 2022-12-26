import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from fastapi import FastAPI

from app.resource import news


def create_app():
    app = FastAPI(title="Rest API", description="Thais Carvalho")
    news.init_app(app=app)
    return app


if __name__ == "app.main":
    app = create_app()
