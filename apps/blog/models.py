from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  