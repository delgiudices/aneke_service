from aneke_service.models import AnekeModel
from django.db import models


class Company(AnekeModel):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=80)


class Category(AnekeModel):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=80)


class Product(AnekeModel):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField()
    company = models.ForeignKey(Company)
    category = models.ForeignKey(Category)
