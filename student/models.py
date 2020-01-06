from django.db import models

# Create your models here.
class studentinfo(models.Model):
    firstname = models.CharField(max_length=20,null=True,blank=True)
    lastname = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20,null=True,blank=True)
    dob = models.DateField(max_length=20,null=True,blank=True)
    gender = models.CharField(max_length=20,null=True,blank=True)






