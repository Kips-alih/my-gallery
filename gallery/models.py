from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length=30)
     
    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    #image field
    image = CloudinaryField('image')
    category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__name__icontains=search_term)
        return gallery
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,title, description):
        self.title = title
        self.description = description
        self.category = category
        self.save()
