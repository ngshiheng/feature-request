# Feature Request App

Build a web application that allows the user to create "feature requests" using Django Framework.

This application is built and tested on Ubuntu.

## Description
- This project was hosted on DigitalOcean.
- Django is used as the server framework of this application 
- PostgreSQL database is used in production while SQLite is used during development
- Gunicorn application server is configured to interface with this application
- Nginx is used to reverse proxy to Gunicorn, giving us access to its security and performance features to serve this application

## Project Management Tool

In this project, I use Trello to track and organize my tasks and features

[My Trello link](https://trello.com/b/bhlakh3D/django-feature-request) 


## Installation

This application was built using:
- Django 2.2.3
- Python 3.7.3

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
```bash
sudo -H pip3 install --upgrade pip
```

## Usage (Development)

Follow the steps below to run locally.

It is best to use the Python virtualenv tool to build locally:
```bash
sudo -H pip3 install virtualenv
virtualenv venv-feature-request
source venv-feature-request/bin/activate
pip install -r requirements.txt
```
Update your settings.py DEBUG to True:
```python
DEBUG = True
```
Migrate the initial database schema to the SQLite database using the management script:
```python
python manage.py makemigrations
python manage.py migrate
```
Create an administrative user:
```python
python manage.py createsuperuser
```

Run the server locally:
```python
python manage.py runserver
```


## Usage (Production)

This project was hosted on DigitalOcean.

You should have a fresh Ubuntu server instance with a non-root user with sudo privileges configured.

After setting up a server with DigitalOcean, proceed with:
[How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
