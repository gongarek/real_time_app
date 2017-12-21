# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0014_signup_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='prezentacja',
            field=models.CharField(default=datetime.datetime(2017, 2, 14, 17, 48, 45, 586180, tzinfo=utc), max_length=360),
            preserve_default=False,
        ),
    ]
