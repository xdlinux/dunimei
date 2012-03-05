from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink

from idios.models import ProfileBase
from places.models import Place

class Profile(ProfileBase):
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True, verify_exists=False)
    bio = models.CharField(_("bio"), blank=True, max_length=140)
    place = models.ForeignKey(Place, null=True, blank=True, related_name='all_users')
    
    @property
    def username(self):
        return self.user.username    