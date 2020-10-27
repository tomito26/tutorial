from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    image = CloudinaryField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    published= models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
    
    
    
    