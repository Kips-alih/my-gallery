from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    #image field
    image = CloudinaryField('image')
