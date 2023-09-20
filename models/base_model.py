#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from uuid import uuid4
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from datetime import datetime
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
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        # each new instance created is added to the storage variable __objects because
        if kwargs:
            for keys, val in kwargs.items():
                if keys in ("created_at", "updated_at"):
                    val = datetime.strptime(kwargs['updated_at'],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                if "__class__" not in keys:
                    setattr(self, keys, val)

    def __str__(self):
        """ prints instance attributes """
        dict_ = self.to_dict()
        cls = str(type(self)).split('.')[-1].split('\'')[0]
        return "[{:s}] ({:s}) {}".format(cls, self.id,
                                         dict_)


    def save(self):
        """update: update_at timestamp"""
        self.updated_at = datetime.utcnow()
        # only when we save the instance, its writen into the json file and then.
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary of keys/values of the instance s"""
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
