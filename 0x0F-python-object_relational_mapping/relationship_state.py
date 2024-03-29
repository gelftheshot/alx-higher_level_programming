#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base


class State(Base):
    """
    State class for table states

    Attributes:
        __tablename__ (str): The table name of the class
        id (sqlalchemy.Integer): The state's id
        name (sqlalchemy.String): The state's name
    """

    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
