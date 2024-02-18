# file: appName/models.py

from django.db import models

# Create your models here.

# company info 
# products 
class Author(models.Model):
   author  = models.CharField(max_length=100)
   

   def __str__(self) -> str:
      return self.author

class Book(models.Model):
   book = models.CharField(max_length=100)
   product_description = models.TextField()   
   Author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
   image  = models.ImageField(null=True)
   price   = models.CharField(max_length=100, null=True)
   date   = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self) -> str:
      return self.book
   
   
