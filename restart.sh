#!/bin/bash

PROJECT_DIR=/home/ec2-user/Inception
MANAGE_PY=${PROJECT_DIR}/manage.py
echo Project Dir ${PROJECT_DIR}

# kill existing one
kill $(ps aux | grep 'Inception/manage.py' | awk '{print $2}')

# cd to project folder
cd ${PROJECT_DIR}
source venv/bin/activate
git pull
pip install -r requirements.txt
bower install
python manage.py collectstatic --noinput

nohup python ${MANAGE_PY} runserver 0.0.0.0:8787 >/dev/null 2>&1 &

echo Restart Finish!