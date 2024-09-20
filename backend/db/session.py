from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URl = settings.DATABASE_URL
print(f"DB: {SQLALCHEMY_DATABASE_URl}")
engine = create_engine(SQLALCHEMY_DATABASE_URl)


SEASSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)



