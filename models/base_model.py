#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False
                        )
    updated_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False
                        )

    def __init__(self, *args, **kwargs):
        """ init BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        # each new instance created is added to the storage variable __objects
        if kwargs:
            for key, val in kwargs.items():
                if key in ("created_at", "updated_at"):
                    val = datetime.strptime(kwargs['updated_at'],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """ prints instance """
        dict = self.to_dict()
        cls = str(type(self)).split('.')[-1].split('\'')[0]
        return "[{:s}] ({:s}) {}".format(cls, self.id,
                                         dict)

    def save(self):
        """update: update_at"""
        self.updated_at = datetime.utcnow()
        # only when we save the instance, its writen into the json file
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary of keys/values of the instance"""
        dictionary = {}
        dictionary.update(self.__dict__)
        try:
            del dictionary['_sa_instance_state']
        except Exception:
            pass
        dictionary.update({'__class__': (str(type(self))
                                         .split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

    def delete(self):
        """ deletes object from storage """
        models.storage.delete(self)
