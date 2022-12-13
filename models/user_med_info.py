#!/usr/bin/python3

from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Integer, Column, ForeignKey, Float


class UserMedInfo(BaseModel, Base):
    """contains the biodata of a user
    first_name, Last_name, age, weight, height, genotype, blood-group
    """
    __tablename__ = 'biodata'
    med_id = Column(String(70), ForeignKey('login.id'), nullable=False)
    first_name = Column(String(75), nullable=False)
    last_name = Column(String(75), nullable=False)
    genotype = Column(String(4), nullable=False)
    blood_group = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)
    allergies = Column(String(450), nullable=True) 
