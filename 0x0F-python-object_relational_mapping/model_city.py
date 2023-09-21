#!/usr/bin/python3
'''Module contains the class definition of a City'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    '''class definition of a City'''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
