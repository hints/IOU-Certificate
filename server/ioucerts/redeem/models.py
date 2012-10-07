from django.db import models

# Create your models here.

class Users(models.Model):
  seed = models.IntegerField()
  generated = models.IntegerField()
  email = models.CharField(max_length=64)

class Certs(models.Model):
  user = models.ForeignKey(Users)
  token = models.CharField(max_length=6)
  status = models.CharField(max_length=6)
  amount = models.IntegerField()
  redeemer_email = models.CharField(max_length=64)

