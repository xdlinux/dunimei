from django.db import models
from django.contrib.auth.models import User


class Bid(models.Model):
    """the book model"""
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    authors = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.title


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


class Book(models.Model):
    """"""
    bid = models.ForeignKey(Bid)
    current_record = models.ForeignKey('Record',
                                    related_name="current_record",
                                    blank=True)

    def __unicode__(self):
        return u"Item"


class Record(models.Model):
    """the record model"""
    book = models.ForeignKey(Book)
    owner = models.ForeignKey(User, related_name="owner_of")
    lendto = models.ForeignKey(User, related_name="lender_of")
    lenddate = models.DateField()
    deadline = models.DateField()
