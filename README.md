# Questioner
Bootcamp project



[![Build Status](https://travis-ci.org/Astro2030/Questioner.svg?branch=develop)](https://travis-ci.org/Astro2030/Questioner) [![Coverage Status](https://coveralls.io/repos/github/Astro2030/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/Astro2030/Questioner?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/d47e0121aee0393fd5f8/maintainability)](https://codeclimate.com/github/Astro2030/Questioner/maintainability)



Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize
questions to be answered. Other users can vote on asked questions and they bubble to the top
or bottom of the log. The application has two roles, the Administrator role and regular users roles.The administrator is responsible for creating meetups,deleting meetups, add images and tags to a meetup. A regular user is basically a normal user of the system. He/she's able to view meetups, confirm attendance on a meetup, ask questions on a specific meetup, comment on a question in a meet up and upvoting or downvoting a meetup.


# Meetups API Endpoints

URL Endpoint                          | HTTP Request   |  Description                     | Access         |
-----------------------------------   | -------------  | -----------------------          |--------------- |
api/v1/meetups/upcoming                |     GET        |  Retrieves all upcoming meetups            |  Public        |
api/v1/meetup/<int:meetup_id>         |     GET        |  Retrieves a specific meetup     |  Public        |
/meetups/<meetup_id>/rsvps|     POST       |  Confirms attendance to a meetup |  public        |
api/v1/meeetups   |    POST    |    Creates meetups   | private |

# Questions API Endpoints

URL Endpoint                          | HTTP Request   |  Description                     | Access         |
-----------------------------------   | -------------  | -----------------------          |--------------- |
/meetups/<meetup_id>/questions   |     GET        |  Retrieves a specific meetup     |  Public        |
/meetups/<meetup_id>/questions/<question_id>/upvote |  post   |    upvotes a question | public    |
/meetups/<meetup_id>/questions/<question_id>/downvote | post  |   Downvotes a question| public    |

# Authentication Endpoints

URL Endpoint                          | HTTP Request   |  Description                     | Access         |
-----------------------------------   | -------------  | -----------------------          |--------------- |
api/v1/auth/register                      |     POST        |  Registers users            |  Public        |
api/v1/auth/login    |     POST       |  Log's in a user     |  Public        |

# Installing the Application Locally
To use the application locally, please proceed as follows: Before running the application:

-Install Postgres 10.1. Read More


Running the application.

*Git clone the repo, cd into the repo*

*configure virtual environment.*

*Configure your environmental variables from the API/.env file as desired, example, JWT_SECRET=<your-secret> to change the JWT_SECRET of the application.*
  
*run source API/.env to configure environmental variables*

*run source venv/bin/activate to activate your virtual environment*

*run pip install -r requirements.txt to install dependencies.*

*run gunicorn API.run:app to run the application*

  
# Testing the application.

The cloned repo has a number of tests included for the testing against the application. To run the included tests automatically,

*run pytest to run using pytest only.*

*run coverage run --source /app/api/v1/ -m pytest app/tests/v1 -q*

*The application can also be tested using Postman.*


