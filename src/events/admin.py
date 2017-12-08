# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event
from .forms import EventForm


def make_akceptacja(modeladmin, request, queryset):
    queryset.update(status='a')
make_akceptacja.short_description = "zaznacz, by zaakceptowac"

def make_niezaakceptowany(modeladmin, request, queryset):
    queryset.update(status='n')
make_niezaakceptowany.short_description = "zaznacz, by niezaakceptowac"





class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes', 'status']
    form = EventForm
    actions = [make_akceptacja, make_niezaakceptowany]

admin.site.register(Event, EventAdmin )