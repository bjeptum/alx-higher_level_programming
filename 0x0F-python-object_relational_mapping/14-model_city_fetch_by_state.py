#!/usr/bin/python3
"""
Prints all Cities from the database
"""

from sys import argv
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == '__main__':

    # Connect to MySQL server running on localhost
    username, password, database = argv[1], argv[2], argv[3]

    # Create engine and connect to db
    engine = create_engine(f'mysql+mysqldb://{username}:\
                             {password}@localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database and print results
    results = session.query(City).order_by(City.id).all()
    for city in results:
        state = session.query(State).filter(State.id == city.state_id).first()
        print(f"{state name}: {city.id} {city.name}")
