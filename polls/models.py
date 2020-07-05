from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=30)
    detail = models.TextField()
    stock = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=30)
    detail = models.TextField()
    stock = models.CharField(max_length=20)

    def __str__(self):
        return self.name
