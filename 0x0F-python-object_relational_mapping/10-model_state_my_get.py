#!/usr/bin/python3
"""
A script that prints the state passed as an argument if it is dbase
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """access dbase to filter out state passed as argument"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first()
    if states is not None:
        print('{0}'.format(states.id))
    else:
        print("Not found")
