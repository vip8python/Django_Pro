from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    descriptions = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        pass


