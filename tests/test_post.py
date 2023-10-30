from lib.post import *

"""
post constructs with an id, postname and email
"""
def test_post_constructs():
    post = Post(1, "Test title", "test content", 100, 1)
    assert post.id == 1
    assert post.title == "Test title"
    assert post.content == "test content"
    assert post.views == 100
    assert post.user_id == 1

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "Test post", "Test content", 100, 1)
    assert str(post) == "Post(1, Test post, Test content, 100, 1)"
    # Try commenting out the `__repr__` method in lib/post.py
    # And see what happens when you run this test again.

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test post", "Test content", 100, 1)
    post2 = Post(1, "Test post", "Test content", 100, 1)
    assert post1 == post2

    