# Use python image
FROM python:3
ENV PYTHONUNBUFFERED  1

RUN mkdir /code

WORKDIR /code

# Copy requirements.txt to code and install library via the text file.
ADD requirements.txt /code/

RUN pip install -r requirements.txt

RUN pip install -r requirements.txt
ADD . /code/

