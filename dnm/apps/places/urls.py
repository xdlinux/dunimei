from django.conf.urls.defaults import *

urlpatterns = patterns("places.views",
    url(r'^(?P<slug>[-\w]+)/$', 'place', name='place'),
)
