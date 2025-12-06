from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_url = "postgresql://postgres:admin@localhost:5432/product"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush= False, autocommit=False, bind=engine)
Base = declarative_base()