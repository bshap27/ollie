# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intakeform', '0003_auto_20171007_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='userprofile_id',
            new_name='userprofile',
        ),
    ]
