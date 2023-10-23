#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """class User"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user', cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """ init user """
        super().__init__(*args, **kwargs)
