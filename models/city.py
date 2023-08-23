#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    __tablename__= 'cities'
    name = Column(String (128), nullable=False)
    state_id = Column(String (60), nullable=False, ForeignKey('states.id'))
    
     """ relationship with the class Place """
    places = relationship(Place, cascade='all, delete' backref='cities')
