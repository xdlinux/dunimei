from django.db import models
from django.contrib.auth.models import User
from books.models import Place

class UserProfile(models.Model):
    """hold the user's profile info"""
    user = models.OneToOneField(User)
    bio = models.CharField(blank=True, max_length=140)
    webpage = models.URLField(blank=True, verify_exists=False)
    phone = models.CharField(max_length=11)
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return u'profile'

        
