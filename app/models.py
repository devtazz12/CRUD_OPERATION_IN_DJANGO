from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name=models.CharField(max_length=100)
    ctg_slug = AutoSlugField(populate_from ='name')
    
    class Meta:
        ordering =['id']
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='ctg' )
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    
    
    
    class Meta:
        ordering =['-id']
        
    def __str__(self):
        return self.name
    

# employees model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=100)
    phone = models.IntegerField()
    
    
    def __str__(self):
        return self.name