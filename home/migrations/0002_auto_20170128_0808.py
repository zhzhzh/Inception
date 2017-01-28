# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-28 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='grade',
            field=models.SmallIntegerField(choices=[(1, b'\xe5\x8d\x95\xe7\xae\xad\xe5\xa4\xb4'), (2, b'\xe5\xa4\xa9\xe7\x8e\x8b\xe5\xb7\xa8\xe6\x98\x9f'), (3, b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98'), (4, b'\xe5\x90\x8e\xe9\x98\xb2\xe4\xb8\xad\xe5\x9d\x9a'), (5, b'\xe9\xab\x98\xe6\x95\x88\xe5\x89\x8d\xe5\x9c\xba'), (6, b'\xe9\x9d\xa0\xe8\xb0\xb1\xe5\x90\x8e\xe5\x9c\xba'), (7, b'\xe4\xb8\xad\xe8\xa7\x84\xe4\xb8\xad\xe7\x9f\xa9'), (8, b'\xe8\x83\x8c\xe9\x94\x85\xe4\xb8\x80\xe6\xb4\xbe')], default=0, verbose_name=b'\xe7\x90\x83\xe5\x91\x98\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='member',
            name='pos1',
            field=models.CharField(choices=[(b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98', b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98'), (b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab', b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab', b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe5\x89\x8d\xe9\x94\x8b', b'\xe5\x89\x8d\xe9\x94\x8b'), (b'\xe7\x89\xb9\xe6\xae\x8a', b'\xe7\x89\xb9\xe6\xae\x8a')], max_length=32, verbose_name=b'\xe7\xac\xac\xe4\xb8\x80\xe4\xbd\x8d\xe7\xbd\xae'),
        ),
        migrations.AlterField(
            model_name='member',
            name='pos2',
            field=models.CharField(choices=[(b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98', b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98'), (b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab', b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab', b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe5\x89\x8d\xe9\x94\x8b', b'\xe5\x89\x8d\xe9\x94\x8b'), (b'\xe7\x89\xb9\xe6\xae\x8a', b'\xe7\x89\xb9\xe6\xae\x8a')], max_length=32, null=True, verbose_name=b'\xe7\xac\xac\xe4\xba\x8c\xe4\xbd\x8d\xe7\xbd\xae'),
        ),
        migrations.AlterField(
            model_name='member',
            name='pos3',
            field=models.CharField(choices=[(b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98', b'\xe5\xae\x88\xe9\x97\xa8\xe5\x91\x98'), (b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab', b'\xe4\xb8\xad\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab', b'\xe8\xbe\xb9\xe5\x90\x8e\xe5\x8d\xab'), (b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe9\x98\xb2\xe5\xae\x88\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba', b'\xe6\x94\xbb\xe5\x87\xbb\xe5\x9e\x8b\xe4\xb8\xad\xe5\x9c\xba'), (b'\xe5\x89\x8d\xe9\x94\x8b', b'\xe5\x89\x8d\xe9\x94\x8b'), (b'\xe7\x89\xb9\xe6\xae\x8a', b'\xe7\x89\xb9\xe6\xae\x8a')], max_length=32, null=True, verbose_name=b'\xe7\xac\xac\xe4\xb8\x89\xe4\xbd\x8d\xe7\xbd\xae'),
        ),
    ]
