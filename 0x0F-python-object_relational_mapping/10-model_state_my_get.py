#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
"""
a script that select every thing in the student order by it' id
"""
if __name__ == "__main__":
    path = f"mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"

    engine = create_engine(path, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
                    .filter(State.name == sys.argv[4])\
                    .order_by(State.id)\
                    .all()
    if states:
        for state in states:
            print(str(state.id))
    else:
        print("Not found")
    session.close()
