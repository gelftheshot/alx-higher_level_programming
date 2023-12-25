#!/usr/bin/python3
"""
contains the class definition of a city and an instance
Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """
        represents the class class the is connected to
        city table from the database
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True,)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
