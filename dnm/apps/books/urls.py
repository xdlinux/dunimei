from django.conf.urls.defaults import *

urlpatterns = patterns("books.views",
    url(r'^user/(?P<username>\w+)/$','user_book',name='user_book'),
    url(r'^(?P<id>\d+)/$', 'bid_detail', name='bid_detail'),
    url(r'^borrow/(?P<id>\d+)/$', 'borrow_book', name='borrow_book'),
)
