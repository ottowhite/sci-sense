from django.db import models

# Create your models here.
class Question(models.Model):
    spec_point = models.FloatField()
    
    question = models.TextField()
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.CharField(max_length=50)
    d = models.CharField(max_length=50)
    answer = models.CharField(max_length=1)

