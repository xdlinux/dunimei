from django.shortcuts import render_to_response
from django.template import RequestContext
from places.models import Place

def place(request, slug):
    try:
        place = Place.objects.get(slug=slug)
    except Place.DoesNotExist:
        raise Http404
    users = place.all_users.all()
    return render_to_response('places/place.html',
                                {'place': place, 'users': users},
                                context_instance=RequestContext(request))
    