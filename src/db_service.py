from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # type:ignore

from config import settings

# `echo` parameter logs all SQLs emitted
engine = create_engine(settings.DATABASE_URI, echo=True, future=True)
Session = sessionmaker(engine)
Base = declarative_base()
