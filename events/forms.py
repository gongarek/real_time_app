from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget
from .widgetcik import SelectTimeWidget

class EventForm(forms.ModelForm):

    day = forms.DateField(widget=SelectDateWidget)
    start_time = forms.TimeField(widget=SelectTimeWidget)
    end_time = forms.TimeField(widget=SelectTimeWidget)
    class Meta:
        model = Event
        fields = ['day', 'start_time', 'end_time', 'notes']

