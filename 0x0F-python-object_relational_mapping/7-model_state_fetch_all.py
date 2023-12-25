#!/usr/bin/python3
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
""" a script that select every thing in the student order by it' id"""

path = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"

engine = create_engine(path)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()

for state in states:
    print(str(state.id) + ':', state.name)