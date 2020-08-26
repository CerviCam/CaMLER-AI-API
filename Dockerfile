FROM cervicam/pytorch

RUN mkdir /app
ADD ./api /app/api
ADD ./project /app/project
ADD ./manage.py /app/manage.py
ADD ./wsgi.py /app/wsgi.py
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt