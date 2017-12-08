# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Zapis', 'verbose_name_plural': 'Zapisy'},
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(default=datetime.datetime(2017, 12, 5, 19, 30, 41, 970701, tzinfo=utc), max_length=1, choices=[('c', 'czeka na akceptacje'), ('a', 'zaakceptowany'), ('n', 'niezaakceptowany')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(help_text='Day of the event', verbose_name='Dzie\u0144 zapisu'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(help_text='Final time', verbose_name='Koniec wizyty'),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(help_text='Textual Notes', null=True, verbose_name='Notatki o pupilu', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(help_text='Starting time', verbose_name='Pocz\u0105tek wyzyty'),
        ),
    ]
