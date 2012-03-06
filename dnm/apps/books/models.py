from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User


class Bid(models.Model):
    """the book model"""
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    authors = models.CharField(max_length=255)
    img = models.URLField(blank=True, verify_exists=True)
    description = models.TextField(max_length=500)
    douban_id = models.CharField(max_length=10, blank=True)
    
    def __unicode__(self):
        return self.title
    
    @property
    def douban_url(self):
        return "http://book.douban.com/subject/%s/" % self.douban_id
    
    def num(self):
        return len(self.book_set.all())

    @permalink
    def get_absolute_url(self):
        return ('bid_detail', None, {'id': self.douban_id })
    


class Book(models.Model):
    """"""
    bid = models.ForeignKey(Bid)
    owner = models.ForeignKey(User)
    #state = models.Bool
    current_record = models.ForeignKey('Record',
                                    related_name="current_record",
                                    null=True,
                                    blank=True)

    def __unicode__(self):
        return '%s'% self.bid.title


class Record(models.Model):
    """the record model"""
    book = models.ForeignKey(Book)
    owner = models.ForeignKey(User, related_name="owner_of")#who owns the book now
    lendto = models.ForeignKey(User, related_name="lender_of")
    lenddate = models.DateField()
    deadline = models.DateField()
    pre_record = models.ForeignKey('Record', null=True)

    def __unicode__(self):
        return u"Record"
