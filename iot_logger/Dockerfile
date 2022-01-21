
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9.5

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /iot_logger

# Set the working directory to /iot_logger
WORKDIR /iot_logger

# Copy the current directory contents into the container at /iot_logger
ADD . /iot_logger/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# run the django server 
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
