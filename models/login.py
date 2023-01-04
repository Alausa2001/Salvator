#!/usr/bin/python3
from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class UserLogin(BaseModel, Base):
    """contain the user login details"""
    __tablename__ = 'login'
    #  user_id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(204), nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    records = relationship('Records', cascade='all, delete-orphan', backref='user')
    medications = relationship('Medication', cascade='all, delete-orphan', backref='user_meds')
    immunizations = relationship('Immunization', cascade='all, delete-orphan', backref='user_vaccines')
    tests = relationship('MedicalTest', cascade='all, delete-orphan', backref='user_tests')
