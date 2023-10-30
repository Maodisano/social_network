-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

-- -- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ( 'mao', 'mao@gmail.com');
INSERT INTO users (username, email) VALUES ( 'leo', 'leo@gmail.com');



DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);


INSERT INTO posts (title, content, views, user_id) VALUES ( 'Title', 'Content', 100, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ( 'New Title', 'new content', 10, 2);