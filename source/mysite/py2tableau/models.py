from django.db import models

# Create your models here.
class Covid(models.Model):
    state = models.CharField(max_length=20)

class User(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
