# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /memoapp

# Set the working directory to /memo
WORKDIR /memoapp
ADD ./requirements.txt /memoapp

# Install any needed packages specified in requirements.txt
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev mariadb-dev\
 postgresql-dev  g++ libgcc libstdc++ libxml2-dev libxslt-dev jpeg-dev && pip install cython \
 && pip install -r requirements.txt
RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*
