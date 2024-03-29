#!/usr/bin/python3
"""This sript defines the user class of the database."""
import models
import sqlalchemy 
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents the MySQL database user class
    Attributes:
        password: User password
        email: User email address
        first_name: User first name
        last_name: User last name
    """
    if models.storage_t == "db":
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
else:
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
