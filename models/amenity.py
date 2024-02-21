#!/usr/bin/python3
"""This script defines the amenity class."""
from models.place import place_amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
class Amenity(BaseModel, Base):
    """Defines the MySQL database amenity class.

    Attributes:
        __tablename__ (str): The tablename for amenity class.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
