-- describe the users schema
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS meetup CASCADE;
DROP TABLE IF EXISTS questions CASCADE;

CREATE TABLE IF NOT EXISTS users
(
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    registered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    email VARCHAR(254) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE index username_index on users (username);
CREATE index email_index on users (email);


-- describe the meetup schema

CREATE TABLE IF NOT EXISTS meetup
(
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR NOT NULL,
    topic VARCHAR NOT NULL,
    questions INT DEFAULT 0,
    description VARCHAR(200) NOT NULL,
    happening_on VARCHAR NOT NULL
);


-- describe the QUESTIONS schema

create table if NOT EXISTS questions
(
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR NOT NULL,
    meetup_id INT NOT NULL,
    title VARCHAR NOT NULL,
    body VARCHAR NOT NULL,
    upvotes INT DEFAULT 0,              
    downvotes INT DEFAULT 0
);

-- INSERT INTO users (firstname, lastname, username, email, password, is_admin) VALUES ('Wycliffe', 'Omari', 'Cliffe', 'omariwycliffe@gmail.com', 
--             'Andela1!!!', True);