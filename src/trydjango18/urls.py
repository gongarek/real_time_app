from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^about/$', 'trydjango18.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),                          # url admina powstal przy migracji
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^recrutation/$', 'newsletter.views.recrutation', name='recrutation'),
    url(r'^records/$', 'events.views.records', name='records'),
    url(r'^listofrecords/$', 'events.views.list_of_records', name='listofrecords'),

]


