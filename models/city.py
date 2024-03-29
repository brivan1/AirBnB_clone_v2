#!/usr/bin/python3
"""This script defines the city class of the database."""
import models
import sqlalchemy
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from models.place import Place
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Defines the MySQL city class
    Attributes:
        state_id: the city class state id
    """
    if models.storage_t == "db":
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
else:
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the city"""
        super().__init__(*args, **kwargs)
