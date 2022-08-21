from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title


class Project(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name='project_creator')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='project_category')
    location = models.CharField(max_length=100, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    deadline = models.DateTimeField(blank=True, null=True)
    favourite = models.ManyToManyField(User, related_name='favourite',default=None,blank=True)
    funding_amount = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='project/tender_images', blank=True, null=True)
    
    
    
