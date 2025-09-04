from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database url
DATABASE_URL = "sqlite:///./toystore.db"

# create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
