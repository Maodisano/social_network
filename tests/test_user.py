from lib.user import *

"""
User constructs with an id, username and email
"""
def test_user_constructs():
    user = User(1, "Test user", "Test email")
    assert user.id == 1
    assert user.username == "Test user"
    assert user.email == "Test email"

"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "Test user", "Test email")
    assert str(user) == "User(1, Test user, Test email)"
    # Try commenting out the `__repr__` method in lib/user.py
    # And see what happens when you run this test again.

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test user", "Test Genre")
    user2 = User(1, "Test user", "Test Genre")
    assert user1 == user2