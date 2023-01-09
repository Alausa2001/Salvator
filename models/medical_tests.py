#!/usr/bin/python3
from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class MedicalTest(BaseModel, Base):
    """contains information about the medical tests of a user"""
    __tablename__ = "MedicalTest"
    test_id = Column(String(256), ForeignKey('login.id'), nullable=False)
    test_type = Column(String(256), nullable=False)
    date = Column(String(256), nullable=False)
    result = Column(String(1024), nullable=False)
    other = Column(String(1024), nullable=True)
