# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_czlonkowie_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='status',
        ),
        migrations.AddField(
            model_name='signup',
            name='wiadomosc',
            field=models.CharField(default=datetime.datetime(2017, 2, 13, 19, 1, 57, 148955, tzinfo=utc), max_length=240),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default=datetime.datetime(2017, 2, 13, 19, 4, 20, 550672, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
