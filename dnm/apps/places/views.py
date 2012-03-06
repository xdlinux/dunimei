from django.shortcuts import render_to_response
from django.template import RequestContext
from places.models import Place
from django.contrib.auth.models import User
from books.models import Bid, Book, Record
from sets import Set

def place(request, slug):
    try:
        place = Place.objects.get(slug=slug)
    except Place.DoesNotExist:
        raise Http404
    users = place.all_users.all()
    bookset=Set([])
    for user in users:
        books = Book.objects.filter(owner=user)
        bookset = bookset | Set(books)
    return render_to_response('places/place.html',
            {'place': place, 'users': users, 'books':bookset},
                                context_instance=RequestContext(request))
    
