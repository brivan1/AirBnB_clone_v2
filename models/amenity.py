#!/usr/bin/python3
"""This script defines the amenity class."""
from models.place import place_amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey

storage_engine = environ.get("HBNB_TYPE_STORAGE")

class Amenity(BaseModel, Base):
    """Defines the MySQL database amenity class.

    Attributes:
        __tablename__ (str): The tablename for amenity class.
    """
    if (storage_engine == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
