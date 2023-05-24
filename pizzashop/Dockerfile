# We will use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /pizza_ordering_service

# Set the working directory to /pizza_ordering_service
WORKDIR /pizza_ordering_service

# Copy the current directory contents into the container at /pizza_ordering_service
ADD . /pizza_ordering_service/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
