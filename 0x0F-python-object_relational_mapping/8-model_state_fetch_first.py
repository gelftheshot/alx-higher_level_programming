#!/usr/bin/python3
"""
lists the first state State objects from the database hbtn_0e_6_usa
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

    first = session.query(State).first()

    if first:
        print(str(first.id) + ':', first.name)
    else:
        print("Nothing")
    session.close()
