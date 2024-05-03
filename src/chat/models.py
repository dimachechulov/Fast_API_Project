from datetime import datetime

import sqlalchemy
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Integer, TIMESTAMP, String, Table, Column, create_engine, UniqueConstraint, ForeignKey, \
    Boolean
from sqlalchemy.orm import sessionmaker, declarative_base



Base = declarative_base()


class Message(Base):
    __tablename__ = 'Message'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

