from django.contrib import admin
# Register your models here.

from .forms import SignUpForm
from .models import SignUp
# from .models import Czlonkowie


def make_akceptacja(modeladmin, request, queryset):
    queryset.update(status='a')
make_akceptacja.short_description = "zaznacz, by zaakceptowac"

def make_niezaakceptowany(modeladmin, request, queryset):
    queryset.update(status='n')
make_niezaakceptowany.short_description = "zaznacz, by niezaakceptowac"

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "full_name", "timestamp", "updated", "status" ] # "akceptacja"]
    form = SignUpForm
    actions=[make_akceptacja, make_niezaakceptowany]

admin.site.register(SignUp, SignUpAdmin )




# class CzlonkowieAdmin(admin.ModelAdmin):
#     list_display = [ "__unicode__",]  #siep ieprzy
#     class Meta:
#         model = Czlonkowie
#     list_display = [ "__unicode__"]  #siep ieprzy
# admin.site.register(Czlonkowie, CzlonkowieAdmin)
