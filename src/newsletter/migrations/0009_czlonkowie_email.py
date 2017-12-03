# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newsletter.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_czlonkowie'),
    ]

    operations = [
        migrations.AddField(
            model_name='czlonkowie',
            name='email',
            field=models.EmailField(default=datetime.datetime(2017, 1, 10, 6, 30, 54, 588835, tzinfo=utc), max_length=254, verbose_name=newsletter.models.SignUp),
            preserve_default=False,
        ),
    ]
