# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_remove_signup_akceptacja'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='status',
            field=models.CharField(default=datetime.datetime(2017, 1, 4, 2, 34, 18, 221422, tzinfo=utc), max_length=1, choices=[(b'c', b'czeka na akceptacje'), (b'a', b'zaakceptowany'), (b'n', b'niezaakceptowany')]),
            preserve_default=False,
        ),
    ]
