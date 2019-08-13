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

class AppUser(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=64)
    is_teacher = models.BooleanField()

    def __str__(self):
        return f"{self.forename} {self.surname} ({self.username})"