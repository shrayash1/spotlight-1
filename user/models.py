from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = (
        ('Creator', 'Creator'),
        ('Investor', 'Investor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    contact = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    backed_projects = models.IntegerField(null=True, blank=True)
    amount_spent = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
