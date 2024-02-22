#!/usr/bin/python3
"""This script defines the Place class of MySQL."""
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
import models
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))
class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: the city id
        user_id: the user id
        name: first and last name input
        description: description
        number_rooms:the number of rooms(integer)
        number_bathrooms: the number of bathrooms(integer)
        max_guest: the maximum number of guests
        price_by_night:: the price per night
        latitude: latitude
        longitude: longitude
        amenity_ids: the Amenity id list
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ this defines reviews"""
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.place_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def amenities(self):
            """this defines amenities """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ the amenities setter"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
