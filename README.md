# Inception

Site: http://54.200.14.34:8787

### Install guide:
1. git clone
2. cd to the project folder
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
bower install
python manage.py migrate
python runserver 0.0.0.0:8787
```

### Member data sync
member data backup into file member.csv

##### to save data from DB to member.csv
cd to project folder and input following command
```
source venv/bin/activate
python manage.py backup_members
```

###### to update data from member.csv to DB
cd to project folder and input following command
```
source venv/bin/activate
python manage.py update_members
```


### Admin
```
source venv/bin/activate
python manage.py createsuperuser

```

admin/admin
