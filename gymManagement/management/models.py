from django.db import models

# Create your models here.
class signupdata(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    password1= models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    
    
class contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    concern = models.TextField(max_length=100)
    
