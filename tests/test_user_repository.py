from lib.user_repository import *
from lib.user import *


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) 

    users = repository.all()

    # Assert on the results
    assert users == [
                    User(1, 'mao', 'mao@gmail.com'),
                    User(2, 'leo', 'leo@gmail.com')]
    
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, 'leo', 'leo@gmail.com')

def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "Shirin", "shirin@gmail.com"))

    result = repository.all()
    assert result == [  
                    User(1, 'mao', 'mao@gmail.com'),
                    User(2, 'leo', 'leo@gmail.com'),
                    User(3, "Shirin", "shirin@gmail.com")
]
    
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(2) 

    result = repository.all()
    assert result == [ 
                    User(1, 'mao', 'mao@gmail.com')]

