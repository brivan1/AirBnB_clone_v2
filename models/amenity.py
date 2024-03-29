#!/usr/bin/python3
"""This script defines the amenity class."""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer

storage_engine = environ.get("HBNB_TYPE_STORAGE")

class Amenity(BaseModel, Base):
    """representstion of amenity"""
    if models.storage_t == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ initializes Amenity"""
        super().__init__(*args, **kwargs)
