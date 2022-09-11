#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')

    else:
        @property
        def cities(self):
            """return new_list"""
            new_list = []

            value = models.storage.all(City).values()
            for i in value:
                if self.id == i.state_id:
                    new_list.append(i)

            return new_list
