from core.config import settings
from db.base_class import Base
from db.session import engine
from fastapi import FastAPI


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, versions=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello():
    return {"msg": "Hello 💃"}
