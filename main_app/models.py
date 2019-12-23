from django.db import models

class Question(models.Model):
    # defining the multiple-choice question table with the django ORM
    spec_point = models.FloatField()
    
    question    = models.TextField()
    diagram     = models.BooleanField(default=False)
    a           = models.CharField(max_length=50)
    b           = models.CharField(max_length=50)
    c           = models.CharField(max_length=50)
    d           = models.CharField(max_length=50)
    answer      = models.CharField(max_length=1)

class Term(models.Model):

    spec_point      = models.FloatField()
    term            = models.TextField()
    definition      = models.TextField()
