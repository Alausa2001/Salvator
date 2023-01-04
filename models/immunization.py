from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Immunization(BaseModel, Base):
    """contains infomation about the immunizations received by a
    patient"""
    __tablename__ = "immunization"
    immunization_id = Column(String(77), ForeignKey('login.id'), nullable=False)
    immunization_name = Column(String(256), nullable=False)
    vaccine_name = Column(String(104), nullable=True)
    date = Column(String(256), nullable=False)
    expiration_date = Column(String(256), nullable=True)
    others = Column(String(1024), nullable=True)
