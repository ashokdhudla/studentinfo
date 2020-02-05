from django.db import models

# Create your models here.


class studentinfo(models.Model):
    firstname = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=30, null=False, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.email)


class addmarks(models.Model):
    id_no = models.IntegerField(null=True, blank=True)
    maths = models.IntegerField(null=True, blank=True)
    physics = models.IntegerField(null=True, blank=True)
    chemistry = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id_no)








