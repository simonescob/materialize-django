# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0007_auto_20161127_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='person',
            new_name='persona',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='ref_person',
            new_name='ref_persona',
        ),
    ]
