-- describe the users schema
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS meetups CASCADE;
DROP TABLE IF EXISTS orders CASCADE;

CREATE TABLE IF NOT EXISTS users
(
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    registered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    password_1 VARCHAR(100) NOT NULL,
    password_2 VARCHAR(100) NOT NULL
);
CREATE index username_index on users (username);
CREATE index email_index on users (email);


-- describe the meetup schema

CREATE TABLE IF NOT EXISTS meetup
(
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR NOT NULL,
    images VARCHAR ARRAY NOT NUL,
    topic VARCHAR NOT NULL,
    description VARCHAR(200) NOT NULL,
    happening_on DATE NOT NULL,
    tags VARCHAR ARRAY NOT NULL
);


-- describe the orders schema

create table if NOT EXISTS questions
(
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_by INT NOT NULL,
    meetup_id INT NOT NULL,
    title VARCHAR NOT NULL,
    body VARCHAR NOT NULL,
    upvotes INT DEFAULT 0,
    downvotes INT DEFAULT 0,
    FOREIGN_KEY (created_by) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN_KEY (meetup_id) REFERENCES meetups(id) ON DELETE CASCADE
);