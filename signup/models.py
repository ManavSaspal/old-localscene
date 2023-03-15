from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
