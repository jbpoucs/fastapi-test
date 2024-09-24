from apis.base import api_router
from core.config import settings
from fastapi import FastAPI


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, versions=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = start_application()


@app.get("/")
def hello():
    return {"msg": "Hello 💃"}
