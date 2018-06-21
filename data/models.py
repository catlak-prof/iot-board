from django.db import models
from django.db import models
from device.models import Device

# Create your models here.
class  Data(models.Model):

    device=models.ForeignKey(Device,related_name="device_data",on_delete=models.CASCADE)

    alan1=models.CharField(max_length=20,blank=True,null=True)
    alan2=models.CharField(max_length=20, blank=True, null=True)
    alan3=models.CharField(max_length=20,blank=True,null=True)
    alan4=models.CharField(max_length=20,blank=True,null=True)
    alan5=models.CharField(max_length=20,blank=True,null=True)
    alan6=models.CharField(max_length=20,blank=True,null=True)
    alan7=models.CharField(max_length=20,blank=True,null=True)
    alan8=models.CharField(max_length=20,blank=True,null=True)

