FROM python:3.5
RUN mkdir /django18
WORKDIR /django18
ADD requirements.txt /django18/
RUN pip install -r requirements.txt
