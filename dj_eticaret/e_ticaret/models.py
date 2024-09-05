from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model): #name, description , price ,stock ,image
   name = models.CharField(max_length=200)
   description = models.TextField()
   price = models.DecimalField(max_digits=10,decimal_places=2)
   stock = models.IntegerField()
   image = models.ImageField(upload_to="")
   
   
   def __str__(self):
       return self.name  
    
class Cart(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    products = models.ManyToManyField(Product , blank=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.user.username}'s Cart"
    
