import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from guvicorn_logger import Logger

from app.resource import news


def create_app():
    app = FastAPI(title="Rest API", description="Thais Carvalho")
    app.add_middleware(CorrelationIdMiddleware)
    Logger(use_colors=False).configure()
    news.init_app(app=app)
    return app


if __name__ == "app.main":
    app = create_app()
