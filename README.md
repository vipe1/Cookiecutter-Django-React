# Cookiecutter Django React
>Cookiecutter created for speeding up the process of creating Django + React project.

## Table of contents:
- [General info](#general-info)
- [Usage](#usage)
- [Developing locally](#developing-locally)
- [Deployment (not yet available)](#deployment)
- [Inspirations](#inspirations)

## General info
Versions of frameworks used to generate this project are:

 - Django - 4.0
 - React - 17.0.2

Project aims to make starting Django + React project as easy as it can be.
Django REST Framework is used to convert Django project to REST API.

## Usage
First, install cookiecutter:
`$ pip install cookiecutter`
Then run:
`$ cookiecutter https://github.com/vipe1/Cookiecutter-Django-React`

## Developing locally
Local development is powered by Docker.
To start developing your project all you need to do is ensure that you have docker and docker-compose working on your machine

To start up the development server run: 
```
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up
```
If you don't want to add `-f local.yml` every time you run commands set environmental variable: `COMPOSE_FILE=local.yml`
Then you can run compose like this:
```
$ docker-compose build
$ docker-compose up
```


## Inspirations
Project is inspired and partly based on:

 - [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
 - [cookiecutter-react-django](https://github.com/ohduran/cookiecutter-react-django)
 - [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest)

If you get confused with how some things work you can go to these repos and read their source. 
