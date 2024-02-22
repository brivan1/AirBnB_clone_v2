#!/usr/bin/python3
"""This script defines review class."""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel, Base):
    """This represents the Review class
    Attributes:
    place_id: place id of review
    user_id: user id of review
    text: description of review
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
