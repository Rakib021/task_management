from django.db import models


# Create your models here.

class TaskStoreModel(models.Model):
    CATEGORY = (
    ('low', 'low'),
    ('medium', 'medium'),
    ('high', 'high'),
    
    )
    

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    priority = models.CharField(max_length=30, choices=CATEGORY)
    
    first_pub = models.DateTimeField(auto_now_add=True) 
    last_pub = models.DateTimeField(auto_now=True) 

