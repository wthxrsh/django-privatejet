from django.db import models

class Contact (models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Message = models.TextField(max_length=100)
    def __str__(self):
        return self.Name;
# Create your models here.
