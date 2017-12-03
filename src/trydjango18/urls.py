from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin                                                       #django.contrib.admin klasa potrzebna do stworzenia url, stworzona automatyzcnie przy migracji


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^recrutation/$', 'newsletter.views.recrutation', name='recrutation'),
    url(r'^about/$', 'trydjango18.views.about', name='about'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),                                          # url admina powstal przy migracji
    url(r'^accounts/', include('registration.backends.default.urls')),
]


