from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    descriptions = models.TextField(max_length=1000)
    image = models.ImageField(blank=True, upload_to='images')
    objects = models.Manager()


    def __str__(self):
        return self.name


