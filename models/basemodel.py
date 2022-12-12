#!/usr/bin/python3

from datetime import datetime
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel:
    """this class contains the general attributes
    id
    created_at : time an instance was created
    updated_at : time an instance was updated
    """
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())


