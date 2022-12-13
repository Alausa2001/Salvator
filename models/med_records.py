#!/usr/bin/python3
import models
from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Records(BaseModel, Base):
    """contains the medical records of a user"""
    __tablename__ = "records"
    records_id = Column(String(70), ForeignKey('login.id'), nullable=False)
    date = Column(String(40), nullable=True)
    diagnosis = Column(String(450), nullable=False)
    prescription = Column(String(450), nullable=True)
    hospital = Column(String(450), nullable=True)
    doctor_name = Column(String(450), nullable=True)
    doctor_contact = Column(String(450), nullable=True)
