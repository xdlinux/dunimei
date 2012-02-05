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

    def __unicode__(self):
        return u"Record"

