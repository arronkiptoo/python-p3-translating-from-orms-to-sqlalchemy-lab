# dog.py
from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    # Create tables in the database
    base.metadata.create_all(engine)

def save(session, dog):
    # Save a new dog object to the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Retrieve all dogs from the database
    return session.query(Dog).all()

def find_by_name(session, name):
    # Find a dog by its name
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, dog_id):
    # Find a dog by its ID
    return session.query(Dog).filter_by(id=dog_id).first()

def find_by_name_and_breed(session, name, breed):
    # Find a dog by its name and breed
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    # Update the breed of a specific dog
    dog.breed = new_breed
    session.commit()

# Example usage
if __name__ == "__main__":
    # Assuming you have an SQLite database
    SQLITE_URL = "sqlite:///dogs.db"
    engine = create_engine(SQLITE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example dog
    joey = Dog(name="joey", breed="cocker spaniel")

    # Save the dog
    save(session, joey)

    # Get all dogs
    all_dogs = get_all(session)
    print("All Dogs:", all_dogs)

    # Find by name
    conan = find_by_name(session, 'conan')
    print("Dog found by name:", conan)

    # Find by ID
    dog_1 = find_by_id(session, 1)
    print("Dog found by ID:", dog_1)

    # Find by name and breed
    fanny = find_by_name_and_breed(session, 'fanny', 'cockapoo')
    print("Dog found by name and breed:", fanny)

    # Update breed
    update_breed(session, joey, 'bulldog')
    updated_record = find_by_name(session, 'joey')
    print("Updated record:", updated_record)
