# Questioner
Bootcamp project



[![Build Status](https://travis-ci.org/Astro2030/Questioner.svg?branch=develop)](https://travis-ci.org/Astro2030/Questioner) [![Coverage Status](https://coveralls.io/repos/github/Astro2030/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/Astro2030/Questioner?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/d47e0121aee0393fd5f8/maintainability)](https://codeclimate.com/github/Astro2030/Questioner/maintainability)



Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize
questions to be answered. Other users can vote on asked questions and they bubble to the top
or bottom of the log. The application has two roles, the Administrator role and regular users roles.The administrator is responsible for creating meetups,deleting meetups, add images and tags to a meetup. A regular user is basically a normal user of the system. He/she's able to view meetups, confirm attendance on a meetup, ask questions on a specific meetup, comment on a question in a meet up and upvoting or downvoting a meetup.


# Meetups API Endpoints

URL Endpoint                          | HTTP Request   |  Description                     | Access         |
-----------------------------------   | -------------  | -----------------------          |--------------- |
api/v1/meetup/upcoming                |     GET        |  Retriees all meetups            |  Public        |
api/v1/meetup/<int:meetup_id>         |     GET        |  Retrieves a specific meetup     |  Public        |
api/v1//meetups/<int:meetup_id>/rsvps |     POST       |  Confirms attendance to a meetup |  public        |

# Questions API Endpoints

URL Endpoint                          | HTTP Request   |  Description                     | Access         |
-----------------------------------   | -------------  | -----------------------          |--------------- |
api/v1/questions                      |     GET        |  Retriees all meetups            |  Public        |
api/v1/questions/<int:question_id>    |     GET        |  Retrieves a specific meetup     |  Public        |

# Installing the Application Locally
To use the application locally, please proceed as follows: Before running the application:

-Install Postgres 10.1. Read More
Configure the database credentials and run create database fast_food_fast_db-

Running the application.

-Git clone the repo, cd into the repo
-configure virtual environment. Read More
-Configure your environmental variables from the API/.env file as desired, example, JWT_SECRET=<your-secret> to change the JWT_SECRET of the application.
-run source API/.env to configure environmental variables
-run source venv/bin/activate to activate your virtual environment
-run pip install -r requirements.txt to install dependencies.
-run gunicorn API.run:app to run the application
  
# Testing the application.
The cloned repo has a number of tests included for the testing against the application. To run the included tests automatically,

run pytest to run using pytest only.
run coverage run --source /API/app/v2/ -m pytest API/tests/v2 -q
The application can also be tested using Postman. Proceed to url localhost:8000` as shown below:

![alt image](https://raw.githubusercontent.com/Astro2030/Questioner/develop/pictures/screenshot1.png)
