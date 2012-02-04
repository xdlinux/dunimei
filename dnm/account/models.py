from django.db import models
from userena.models import UserenaBaseProfile
from django.contrib.auth.models import User
from books.models import Place

class MyProfile(UserenaBaseProfile):
    """hold the user's profile info"""
    user = models.OneToOneField(User, unique=True)
    bio = models.CharField(blank=True, max_length=140)
    webpage = models.URLField(blank=True, verify_exists=False)
    phone = models.CharField(max_length=11)
    place = models.ForeignKey(Place, blank=True)

    def __unicode__(self):
        return self.user.username



