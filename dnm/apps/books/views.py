from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from books.models import Bid, Book, Record

def bid_detail(request, id):
    try:
        bid = Bid.objects.get(douban_id=id)
    except:
        raise Http404
    return render_to_response('books/bid_detail.html',
                                {'bid': bid },
                                context_instance=RequestContext(request))

def user_book(request, username):
    try:
        user = User.objects.get(username__exact=username)
        books = Book.objects.filter(owner=user)
    except:
        raise Http404
    return render_to_response('books/user_book.html',
                              {'books': books, "user": user},
                              context_instance=RequestContext(request))
