from django.conf.urls.defaults import *

urlpatterns = patterns("books.views",
    url(r'^(?P<id>\d+)/$', 'bid_detail', name='bid_detail'),
)
