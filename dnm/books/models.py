from django.db import models

class Book(models.Model):
    """the book model"""
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    authors = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.title

