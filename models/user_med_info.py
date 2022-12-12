#!/usr/bin/python3

from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Integer, Column, ForeignKey, Float


class UserMedInfo(BaseModel, Base):
    """contains the biodata of a user
    first_name, Last_name, age, weight, height, genotype, blood-group
    """
    __tablename__ = 'biodata'
    first_name = Column(String(75), nullable=False)
    last_name = Column(String(75), nullable=False)
    genotype = Column(String(4), nullable=False)
    blood_group = Column(String(2), nullable=False)
    age = Column(Integer, nulable=False)
    height = Column(Float, nullable=True)
    weight = Cloumn(Float, nullable=True)

