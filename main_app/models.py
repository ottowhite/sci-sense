from django.db import models

class Question(models.Model):
    # defining the multiple-choice question table with the django ORM
    spec_point = models.FloatField()
    
    question = models.TextField()
    diagram = models.BooleanField(default=False)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.CharField(max_length=50)
    d = models.CharField(max_length=50)
    answer = models.CharField(max_length=1)

class AppUser(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=25) # this field is temporary; will be replace with hashed password field
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=64)
    is_teacher = models.BooleanField()

    def __str__(self):
        # simply a to_string method to define the description of an object when it is
        # queried in the django shell

        return f"{self.forename} {self.surname} ({self.username})"
