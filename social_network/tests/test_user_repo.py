from lib.user_repo import UserRepository
from lib.user import User

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql") 
    repository = UserRepository(db_connection)
    users = repository.all() # Get all artists
    assert users == [
        User(1, 'abc123', 'abc123@gmail.com'),
        User(2, 'crussell', 'crussell@gmail.com'),
        User(3, 'lizzie95', 'lizzie95@gmail.com')
    ]

def test_create_new_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    assert repository.create(User(4, "marge", "marge@aol.com")) == None
    users = repository.all()
    assert users == [
        User(1, 'abc123', 'abc123@gmail.com'),
        User(2, 'crussell', 'crussell@gmail.com'),
        User(3, 'lizzie95', 'lizzie95@gmail.com'),
        User(4, "marge", "marge@aol.com"),
        ]
    
def test_delete_by_id_number(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    assert repository.delete(2) == None
    users = repository.all()
    assert users == [
        User(1, 'abc123', 'abc123@gmail.com'),
        User(3, 'lizzie95', 'lizzie95@gmail.com')
        ]
