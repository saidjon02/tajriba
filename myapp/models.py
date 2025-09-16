from django.db import models

# Create your models here.
# @tag:nextEditSuggestions

class Post(models.Model):
    image = models.ImageField(upload_to='images/') 
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    text= models.TextField()

    
    def __str__(self):
        return self.title