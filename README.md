## SwachBin Flask API

## Getting started

## Setup

This code works on Python3+ versions.

## Clone the repository

## With Docker:

$ git clone https://github.com/CFC2k22Organisation/SwachBin-Flask-API.git

$ SwachBin-Flask-API/

## Install Docker
https://docs.docker.com/engine/install/ubuntu/

## Build docker image

$ docker build -t swach_dashboard_docker .

Note: ensure in app.py port is mentiond as 8080

$ docker run -it -p 8080:8080 swach_dashboard_docker

In Browser run with 127.0.0.1:8080

## To push:

$docker login

  Username: XXXX
  
  Password: XXXX
  
$ docker tag swach_dashboard_docker swachBin/swach_dashboard_docker:1.0.0

$ docker push swachBin/swach_dashboard_docker:1.0.0

## Without Docker:

## Install the required libraries

$ pip3 install -r requirements.txt

## Clone the repository

$ git clone https://github.com/CFC2k22Organisation/SwachBin-Flask-API.git

$ SwachBin-Flask-API/

## Run app.py

$ python3 app.py 

or

$ python -m flask run

In Browser run with 127.0.0.1:5000

## Live Demo Url:

http://169.51.206.185:31539/




