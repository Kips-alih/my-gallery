from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class category(models.Model):
    category=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.category


class Image(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    #image field
    image = CloudinaryField('image')
    category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    @classmethod
    def search_by_title(cls,search_term):
        gallery = cls.objects.filter(title__icontains=search_term)
        return gallery
    
