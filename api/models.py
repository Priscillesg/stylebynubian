from django.db import models

# Create your models here.

class Favoris(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    business_id =  models.CharField(max_length=140, default='DEFAULT VALUE')
  


    def __str__(self):
        return self.name
    
  
