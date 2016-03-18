from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        #self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.title


# Models for SysRev

class Researcher(models.Model):

    # Link Researcher to Django User
    user = models.OneToOneField(User)

    # forename = models.CharField(max_length=100, null=True, blank=True)
    # surname = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.user.username


class Review(models.Model):
    user            = models.ForeignKey(Researcher)
    title           = models.CharField(max_length=128)
    description     = models.CharField(max_length=128)
    query_string    = models.CharField(max_length=128)

		
    def __unicode__(self):
        return self.title


class Paper(models.Model):
    review          = models.ForeignKey(Review,default=None)
    title           = models.CharField(max_length=128)
    authors         = models.CharField(max_length=128, default=None)
    abstract        = models.CharField(max_length=128)
    date            = models.DateTimeField(auto_now_add=True, blank=True, default=datetime.now)
    query_string    = models.CharField(max_length=128)
    paper_url       = models.URLField(default=None)
    abstract_rev    = models.BooleanField(default=False)
    document_rev    = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Query(models.Model):
    review = models.ForeignKey(Review , null=True)
    string = models.CharField(max_length=128)

    def __unicode__(self):
        return self.review



