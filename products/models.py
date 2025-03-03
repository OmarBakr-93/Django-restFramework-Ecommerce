from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.TextChoices):
  Computer = 'Computer'
  Food = 'Food'
  Kids = 'Kids'
  HOME = 'Home'
  Other = 'Other'
  

class Product(models.Model):
  name = models.CharField(max_length=255, default='', blank=False)
  description = models.TextField(max_length=1000, default='', blank=False)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  brand = models.CharField(max_length=255, default='', blank=False)
  category = models.CharField(max_length=255, choices=Category.choices, blank=False)
  rating = models.DecimalField(max_digits=2, decimal_places=1
  )
  stock = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  
  def __str__(self):
    return self.name