from django.db import models

# Create your models here.


class studentinfo(models.Model):
    firstname = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True, )
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


class Subject(models.Model):
    id_no = models.AutoField(primary_key=True)
    subjectname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id_no)



class fee(models.Model):
    first = models.IntegerField(null=True, blank=True)
    second = models.IntegerField(null=True, blank=True)
    third = models.IntegerField(null=True, blank=True)
    fourth = models.IntegerField(null=True, blank=True)
    fifth = models.IntegerField(null=True, blank=True)
    sixth = models.IntegerField(null=True, blank=True)
    seventh = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.third)


class staff(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)





