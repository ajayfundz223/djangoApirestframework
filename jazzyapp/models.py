from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(default=" ")
    count = 1
    cart = False

    def _str_(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def _str_(self):
        return self.name