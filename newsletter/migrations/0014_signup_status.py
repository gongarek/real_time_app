# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0013_auto_20170214_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='status',
            field=models.CharField(default=datetime.datetime(2017, 2, 14, 17, 44, 31, 270107, tzinfo=utc), max_length=1, choices=[(b'c', b'czeka na akceptacje'), (b'a', b'zaakceptowany'), (b'n', b'niezaakceptowany')]),
            preserve_default=False,
        ),
    ]
