#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
in which it's city foreign key is the same as the state id
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
if __name__ == "__main__":
    path = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    cities = session.query(City)
    for city in cities:
        state_name = session.query(State)\
                            .filter(State.id == city.state_id)\
                            .first()
        print("{}: ({}) {}".format(state_name.name,
                                   city.id,
                                   city.name))
        session.close()
