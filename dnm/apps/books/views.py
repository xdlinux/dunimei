from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from books.models import Bid, Book, Record

def bid_detail(request, id):
    try:
        bid = Bid.objects.get(douban_id=id)
    except:
        raise Http404
    return render_to_response('books/bid_detail.html',
                                {'bid': bid },
                                context_instance=RequestContext(request))

def uid_detail(request,u_id):
    try:
        #book_id=Book.objects.get(owner=u_id
        pass
    except:
        pass
    #return render_to_response('books/uid_detail.html',
    #                           {'u_id':u_id},
    #                           context_instance=RequestContext(request))
    return 'aa'
