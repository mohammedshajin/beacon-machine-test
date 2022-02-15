from statistics import mode
from turtle import color
from django.db import models
from django.contrib.auth.models import User


size_choice = (
    ('S', "small"),
    ('M', "Medium"),
    ('L', "large"),
)

color_choice = (
    ('Red', "Red"),
    ('Yellow', "Yellow"),
    ('Violet', "Violet"),
)

class Product(models.Model):
    name= models.CharField(max_length=150)
    price = models.IntegerField(blank=True)
    material = models.ManyToManyField('Material', blank=True)
    size = models.CharField(choices=size_choice, max_length=150)
    color = models.CharField(choices=color_choice, max_length=150)
    description = models.TextField(max_length=150)
    availabilty = models.BooleanField(default=True)
    createddate = models.DateTimeField(auto_now_add=True)
    wishlist = models.ManyToManyField(User, related_name='Wishlist', default=None, blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



