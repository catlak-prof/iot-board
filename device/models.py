from django.db import models
from django.db import models
from user.models import User

# Create your models here.
class Device(models.Model):
    auther=models.ForeignKey('auth.User',related_name="auther_device",on_delete=models.CASCADE)

    isim=models.CharField(max_length=50)
    olusturma_tarihi=models.DateField()
    aciklama=models.TextField(max_length=100)

    alan1=models.CharField(max_length=20,blank=True,null=True)
    alan2=models.CharField(max_length=20,blank=True,null=True)
    alan3=models.CharField(max_length=20,blank=True,null=True)
    alan4=models.CharField(max_length=20,blank=True,null=True)
    alan5=models.CharField(max_length=20,blank=True,null=True)
    alan6=models.CharField(max_length=20,blank=True,null=True)
    alan7=models.CharField(max_length=20,blank=True, null=True)
    alan8=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.isim


