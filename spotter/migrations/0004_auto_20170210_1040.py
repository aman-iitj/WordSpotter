# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotter', '0003_auto_20170210_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='count',
            new_name='count_n',
        ),
    ]
