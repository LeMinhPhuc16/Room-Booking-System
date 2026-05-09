from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("DATABASE_URL")

engine = create_engine(URL, echo=True)
localSession = sessionmaker(bind=engine, autoflush=True, autocommit=False)

class Base(DeclarativeBase):
    pass