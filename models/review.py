#!/usr/bin/python3
"""This script defines review class."""
import models
import sqlalchemy
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import relationship
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """This represents the Review class
    Attributes:
    place_id: place id of review
    user_id: user id of review
    text: description of review
    """
    if models.storage_t == "db":
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
else:
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
