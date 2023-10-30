from lib.post_repository import *
from lib.post import *

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) 

    posts = repository.all()

    # Assert on the results
    assert posts == [
                    Post(1, 'Title', 'Content', 100, 1),
                    Post(2, 'New Title', 'new content', 10, 2)]
    
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(2)
    assert post == [
                    Post(2, 'New Title', 'new content', 10, 2)
        ]

# def test_create_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = UserRepository(db_connection)

#     repository.create(User(None, "Shirin", "shirin@gmail.com"))

#     result = repository.all()
#     assert result == [  
#                     User(1, 'mao', 'mao@gmail.com'),
#                     User(2, 'leo', 'leo@gmail.com'),
#                     User(3, "Shirin", "shirin@gmail.com")
# ]
    
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = UserRepository(db_connection)
#     repository.delete(2) 

#     result = repository.all()
#     assert result == [ 
#                     User(1, 'mao', 'mao@gmail.com')]
