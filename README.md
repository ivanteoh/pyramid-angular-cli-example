# Pyramid Angular
Example application that uses [Pyramid](https://trypyramid.com/) framework as backend and [Angular](https://angular.io/) project using cli as frontend

# Frontend

This [Angular](https://angular.io/) application is setup using cli.

## Setup

```
$ npm install -g @angular/cli
```

## Create frontend application
Do not need this step as this repo contains them

```
$ ng new frontend
```

## Go to frontend application

```
$ cd frontend
```
## Install and deploy

```
$ np build
```

## Run

```
$ ng serve
```

## Inspect

* Open http://localhost:4200/

## Test

```
$ ng test
```

## Notes

[Angular](https://angular.io/)

# Backend

## Activate virtual environment, for example

```
$ source ../venv/bin/activate
```

## Install

```
$ pip install -e .
```

## Run

```
$ pserve development.ini --reload
```

## Inspect

* Open http://localhost:6543/

## Test

```
$ py.test backend/tests.py -q
```

## Notes

[Pyramid](https://trypyramid.com/)
