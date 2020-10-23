from django.db import models
from django.contrib.auth.models import user 

# Create your models here.
class customer(models.model):
  user = models.OneToOneField(user, on_delete=models.CASCADE null=true, blank=True)
  name = models.models.CharField(max_length=200,null =True)
  email = models.models.CharField(max_length=200,null =True)

  def __str__(self):
    return self.name


class Product(models.Models):
  name = models.models.CharField(max_length=200, null = True)
  price = models.FloatField()
  digital = models.BooleanField(deafault=False, null =True, blank = False)

  def __str__(self):
    return self.name