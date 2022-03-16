# Deployment
> Tutorials and notes for deployment.

## Table of contents:
- [Startup](#startup)
- [COMPOSE_FILE (please read `Important` section)](#composefile)
- [Running commands in containers](#running-commands-in-containers)

## Startup
Deployment is realtively easy and straightforward.
To deploy your project all you need to do is ensure that you have docker and docker-compose working on your machine

To deploy your project on your machine run: 
```
$ docker-compose -f production.yml build
$ docker-compose -f production.yml up
```

## COMPOSE_FILE
If you don't want to add `-f production.yml` every time you run commands,\
you can set environmental variable:\
`COMPOSE_FILE=production.yml`

Then you can run compose like this:
```
$ docker-compose build
$ docker-compose up
```

### Important
Further down the document you may see `(-f production.yml)` in commands.\
If you did set `COMPOSE_FILE` environmental variable, then omit `(-f production.yml)`.\
Otherwise just delete parentheses like so `-f production.yml`.


## Running commands in containers
When you want to run command in container like, i.e. creating app in django run command following this pattern:
```
$ docker-compose run {service_name} {command}
```
Where:
* `{service_name}` is the service you want to run the command, like:
    * django
    * react
    * postgres
    * traefik
* `{command}` is the command you want to run in this container