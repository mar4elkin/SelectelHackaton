# FROM python:3.7.2-alpine3.8
FROM python:3.7

ENV DOCKER=1

COPY . /srv/www/selectelhackaton
WORKDIR /srv/www/selectelhackaton

RUN pip install --upgrade pip \
    && pip install gunicorn \
    && pip install gevent \
    && pip install -r requirements.txt
    # && python /srv/www/weap/manage.py collectstatic