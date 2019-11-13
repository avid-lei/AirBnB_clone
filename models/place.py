#!/usr/bin/python3
"""Place Class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class inherit from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
