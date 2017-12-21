from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp


def home(request):
    title = "Rekrutacja"
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        form.save()
        context = {
            "title": "Dziekujemy"
        }
    if request.user.is_authenticated() :

        queryset = SignUp.objects.filter(status='a')

        context={
            "queryset":queryset
        }
    return render(request,"home.html",context)


def contact(request):
    title = 'Napisz do nas!'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('informacja')             #czy potrzebne? chyba nie :P
        form_full_name = form.cleaned_data.get('nazwa')         #czy potrzebne? chyba nie :P
        subject = 'Kontakt, strona KNA'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s \n przez %s"%(
                             form_full_name,
                             form_message,
                             form_email)
        send_mail(subject,
                 contact_message,
                 from_email,
                 to_email,
                 # html_message=some_html_message
                 fail_silently=False)# True moze sie przydac, gdy bedziemy zapisywac to do bazy danych

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)

def recrutation(request):
    title = "Rekrutacja"
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        form.save()
        context = {
            "title": "Dziekujemy"
        }
    return render(request, "recrutation.html", context)


    
