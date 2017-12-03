# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newsletter.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_czlonkowie_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='czlonkowie',
            name='full_name',
            field=models.CharField(default=datetime.datetime(2017, 1, 10, 6, 42, 20, 871550, tzinfo=utc), max_length=120, verbose_name=newsletter.models.SignUp),
            preserve_default=False,
        ),
    ]
