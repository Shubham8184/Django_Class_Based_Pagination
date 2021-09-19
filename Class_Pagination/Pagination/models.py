from django.db import models

# Create your models here.

class Laptop(models.Model):
    laptopname=models.CharField(max_length=40)
    laptopcompany=models.CharField(max_length=50)
    laptopram=models.CharField(max_length=30)
    laptoprom=models.CharField(max_length=30)
    laptopprice=models.CharField(max_length=30)
    laptopprocessor=models.CharField(max_length=40)

    def __str__(self):
        return self.laptopname