# Game Library API

This is a CRUD that is responsible for insert games list for some users.

## Install dependencies

`pip install -r requirements.txt`

## Running Tests

`python -m pytest test`

## Running the application

`gunicorn --bind 0.0.0.0:8080 wsgi`

## Mongo Configuration

An environment variable is necessary to set the database to persist information.

`DATABASE_URI=mongodb://localhost:27017/`