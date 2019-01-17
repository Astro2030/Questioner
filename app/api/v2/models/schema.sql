-- describe the users schema
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS meals CASCADE;
DROP TABLE IF EXISTS orders CASCADE;

CREATE TABLE IF NOT EXISTS users
(
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    is_admin boolean NOT NULL DEFAULT False
);
CREATE index username_index on users (username);
CREATE index email_index on users (email);


-- describe the meals schema

CREATE TABLE IF NOT EXISTS meals
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    price TEXT NOT NULL,
    description TEXT NOT NULL
);
CREATE index meal_name_index on meals (name);


-- describe the orders schema

create table if NOT EXISTS orders
(
    id SERIAL PRIMARY KEY,
    location TEXT NOT NULL,
    meals TEXT [],
    username TEXT REFERENCES users(username),
    date TIMESTAMP NOT NULL,
    amount INT NOT NULL,
    status TEXT NOT NULL DEFAULT 'New'
);