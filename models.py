from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
   name =models.CharField(max_length=200)

   def __str__(self):
      return self.name
   
class Product(models.Model):
   name = models.CharField(max_length=200)
   price = models.PositiveIntegerField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   img = models.ImageField(blank=True,default='noImage.png')
   details =models.TextField(blank=True, null=True,max_length=1000)
                           

   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
       return reverse('list')