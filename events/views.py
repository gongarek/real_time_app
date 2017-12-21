from django.shortcuts import render
from .forms import EventForm
from .models import Event

# Create your views here.
def records(request):
    title = "Zapisy"
    form = EventForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        form.save()
        context = {
            "title": "Dziekujemy"
        }
    return render(request, "records.html", context)

def list_of_records(request):
    queryset = Event.objects.filter(status='a').order_by('day')
    context={
        "queryset": queryset
    }
    return render(request,"list_of_records.html", context)





