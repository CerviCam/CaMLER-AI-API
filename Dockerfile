FROM nvcr.io/nvidia/pytorch:19.04-py3
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD ./api /app/api
ADD ./project /app/project
ADD ./manage.py /app/manage.py
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod -x manage.py