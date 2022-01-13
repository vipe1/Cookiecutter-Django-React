# Developing locally
> Tutorials and notes for local development.

## Table of contents:
- [Startup](#startup)
- [COMPOSE_FILE (please read `Important` section)](#composefile)
- [Creating Superuser](#creating-superuser)

## Startup
Local development is powered by Docker.
To start developing your project all you need to do is ensure that you have docker and docker-compose working on your machine

To start up the development server run: 
```
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up
```

## COMPOSE_FILE
If you don't want to add `-f local.yml` every time you run commands,\
you can set environmental variable:\
`COMPOSE_FILE=local.yml`

Then you can run compose like this:
```
$ docker-compose build
$ docker-compose up
```

### Important
Further down the document you may see `(-f local.yml)` in commands.\
If you did set `COMPOSE_FILE` environmental variable, then omit `(-f local.yml)`.\
Otherwise just delete parentheses like so `-f local.yml`.


## Creating Superuser
To create superuser run:
```
$ $ docker-compose (-f local.yml) run --rm django python manage.py createsuperuser
```