# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('name_chn', models.CharField(max_length=32, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('nick_name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('number', models.IntegerField(null=True, verbose_name=b'\xe5\x8f\xb7\xe7\xa0\x81')),
                ('pos1', models.CharField(max_length=32, verbose_name=b'\xe7\xac\xac\xe4\xb8\x80\xe4\xbd\x8d\xe7\xbd\xae', choices=[(b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98', b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98'), (b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab', b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab', b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe5\x89\x8d\xe9\x94\x8b', b'\xe5\x89\x8d\xe9\x94\x8b')])),
                ('pos2', models.CharField(max_length=32, null=True, verbose_name=b'\xe7\xac\xac\xe4\xba\x8c\xe4\xbd\x8d\xe7\xbd\xae', choices=[(b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98', b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98'), (b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab', b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab', b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe5\x89\x8d\xe9\x94\x8b', b'\xe5\x89\x8d\xe9\x94\x8b')])),
                ('pos3', models.CharField(max_length=32, null=True, verbose_name=b'\xe7\xac\xac\xe4\xb8\x89\xe4\xbd\x8d\xe7\xbd\xae', choices=[(b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98', b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98'), (b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab', b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab', b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe5\x89\x8d\xe9\x94\x8b', b'\xe5\x89\x8d\xe9\x94\x8b')])),
                ('top_star', models.BooleanField(default=False, verbose_name=b'\xe5\xa4\xa9\xe7\x8e\x8b\xe5\xb7\xa8\xe6\x98\x9f')),
                ('all_pos', models.BooleanField(default=False, verbose_name=b'\xe5\x85\xa8\xe8\x83\xbd\xe6\x88\x98\xe5\xa3\xab')),
                ('stamina', models.BooleanField(default=False, verbose_name=b'\xe4\xbd\x93\xe8\x83\xbd\xe7\x8b\x82\xe9\xad\x94')),
                ('athletic', models.BooleanField(default=False, verbose_name=b'\xe4\xbd\x93\xe6\xa0\xbc\xe8\xbe\xbe\xe4\xba\xba')),
            ],
            options={
                'ordering': ['number'],
                'db_table': 'member',
            },
        ),
    ]