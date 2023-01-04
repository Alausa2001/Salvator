#!/usr/bin/python3
from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Medication(BaseModel, Base):
    """contains user's medication, doage, reason for use,
    start and end dates, additional information"""
    __tablename__ = 'medication'
    medication_id = Column(String(72), ForeignKey('login.id'), nullable=False)
    medication = Column(String(700), nullable=False)
    dosage = Column(String(700), nullable=False)
    diagnosis = Column(String(700), nullable=False)
    start_date = Column(String(70), nullable=False)
    end_date = Column(String(70), nullable=False)
    additional_info = Column(String(1024), nullable=True)
