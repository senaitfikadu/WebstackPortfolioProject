from django.db import models

class Movie(models.Model):
    title =  models.CharField(max_length=100)
    image_link =  models.CharField(max_length=100)
    video_link =  models.CharField(max_length=100)
    description =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
