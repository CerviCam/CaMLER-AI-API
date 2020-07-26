FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD ./server.py /app/server.py
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt