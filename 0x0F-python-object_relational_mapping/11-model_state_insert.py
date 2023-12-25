#!/usr/bin/python3
"""
adding new state to the databse
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    path = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"

    engine = create_engine(path)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
