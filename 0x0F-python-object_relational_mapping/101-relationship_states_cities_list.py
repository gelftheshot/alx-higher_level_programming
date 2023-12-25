#!/usr/bin/python3
"""
    this is code that prints state and city in that state
    the printing is in this format
    <state id>: <state name>
    <tabulation><city id>: <city name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    path = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State)

    for state in states:
        print(str(state.id) + ':', state.name)
        cities = session.query(City).where(City.state_id == state.id)
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))
