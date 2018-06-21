from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    sifre=models.CharField(max_length=50)
    sehir=models.CharField(max_length=20)
