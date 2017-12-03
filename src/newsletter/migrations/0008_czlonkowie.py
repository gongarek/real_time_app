# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_signup_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Czlonkowie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('czlonek', models.ForeignKey(to='newsletter.SignUp')),
            ],
        ),
    ]
