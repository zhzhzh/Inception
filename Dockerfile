FROM python:3.8

LABEL author="Zhagn Jie"

RUN apt-get update && \
    apt-get install -qq -y build-essential libpq-dev --no-install-recommends && \
    apt-get install -y curl && \
    apt-get -y autoclean && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash && \
    apt-get install -y nodejs && \
    npm install -g bower && \
    apt-get clean

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
RUN bower install --allow-root
RUN python manage.py collectstatic --noinput && \
    python manage.py migrate &&\
    python manage.py update_members

EXPOSE 8787
CMD uwsgi --ini uswgi.ini


