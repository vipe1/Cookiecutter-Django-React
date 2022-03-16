# Cookiecutter Django React
>Cookiecutter created for speeding up the process of creating Django + React project.

## Table of contents:
- [General info](#general-info)
- [Usage](#usage)
- [User authentication](#user-authentication)
- [Developing locally (redirect to separate file)](./LOCAL_DEVELOPMENT.md)
- [Deployment (redirect to separate file)](./DEPLOYMENT.md)
- [Inspirations](#inspirations)

## General info
Versions of frameworks used to generate this project are:

 - Django - 4.0
 - React - 17.0.2

* Database used is PostgreSQL 14.1
* Project aims to make starting Django + React project as easy as it can be
* Django REST Framework is used to convert Django project to REST API
* Traefik works as reverse proxy and tls certificate manager

## Usage
First, install cookiecutter:\
`$ pip install cookiecutter`\
Then run:\
`$ cookiecutter https://github.com/vipe1/Cookiecutter-Django-React`

## User authentication
User authentication uses JWT tokens.
It is implemented with:
- Djoser
- djangorestframework Simple JWT

Endpoints documentation:
- [Base endpoints](https://djoser.readthedocs.io/en/latest/base_endpoints.html)
- [JWT endpoints](https://djoser.readthedocs.io/en/latest/jwt_endpoints.html)

## Inspirations
Project is inspired and partly based on:

 - [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
 - [cookiecutter-react-django](https://github.com/ohduran/cookiecutter-react-django)
 - [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest)

If you get confused with how some things work you can go to these repos and read their source. 
