from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
  pass

class Review(models.Model):
  fullname = models.CharField(max_length=255, blank=False, verbose_name='Full name')
  phone = models.CharField(max_length=15, blank=True, verbose_name='Phone Number')
  email = models.EmailField(max_length=255, blank=False, verbose_name='Email Address')
  review = models.TextField(max_length=100000*1000, blank=False)
  datesubmitted = models.DateTimeField(default=timezone.now, verbose_name="Date Submitted")
  
  def __str__(self):
    return f"Suggestion from {self.fullname}{self.email}"