from django.db import models
from django.db.models import permalink


class Place(models.Model):
    """
    the infomation about a place(example: xidian, tsinghua)
    slug: typically the midddle part of the school's domain name, for example
          www.xidian.edu.cn => xidian, www.xahu.edu.cn => xahu, the slug is
          use for url of the place.
    custom_css:  inspire by reddit, the admin of a place can submit a custom
                css to change the look of the page.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=500)
    custom_css = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
        
    @permalink
    def get_absolute_url(self):
        return ('places.views.place', [str(self.slug)])


