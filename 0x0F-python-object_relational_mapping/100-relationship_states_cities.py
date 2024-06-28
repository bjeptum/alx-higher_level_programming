#!/usr/bin/python3
"""
Creates a state with City
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    # Connect to MySQLserver running onlocalhost
    username, password, database = argv[1], argv[2], argv[3]

    # Create engine and bind it to the metadata of the Base class
    engine = create_engine(f'mysql+mysqldb://{username}:\
                             {password}@localhost:3306/{database}')
    Base.metadata.bind = engine

    # Create a sessiom
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and join with State
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print the results
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.commit()
    session.close()
