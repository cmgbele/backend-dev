from django.db import models

# Create your models here.

class Animal(models.Model):
    SPECIE_CHOICES =(
        ('mammal','Mammal'),
        ('amphibian','Amphibian'),
        ('reptile','Reptile'),
        ('pices','Pices'),
        ('aves','Aves'), 
    ) 


    name = models.CharField(max_length=200,unique=True)
    desc = models.TextField() 
    dob = models.DateField() 
    specie = models.CharField(max_length=200,choices=SPECIE_CHOICES)
    population = models.IntegerField(default=0)
    is_extinct = models.BooleanField() 
    pic_url = models.URLField() 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    viewing_price = models.FloatField(null=True,blank=True) 
    def __str__(self):
        return self.name 
     


class Contact(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email= models.EmailField(null=True,blank=True)
    message = models.TextField(null=True,blank=True) 
    date_created = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name
    
 

