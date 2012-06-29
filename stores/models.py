from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    organization = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    store = models.ForeignKey(Store)
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity_available = models.IntegerField(default=1)

    def __unicode__(self):
        return '%s of %s' % (self.name, self.brand.name)
