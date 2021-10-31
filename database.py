import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://aikyol:1@localhost:5432/tiktok"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()
database = databases.Database(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
