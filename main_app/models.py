from django.db import models
from users.models import models as users_models

class Question(models.Model):
    # defining the multiple-choice question table with the django ORM

    # EDGE CASE: RANDOMISE THE ORDER WITH WHICH QUESTIONS ARE DISPLAYED
    question_id = models.AutoField(primary_key=True)
    spec_point  = models.FloatField()
    question    = models.TextField()
    diagram     = models.BooleanField(default=False)
    a           = models.CharField(max_length=50) # which is also the correct answer
    b           = models.CharField(max_length=50)
    c           = models.CharField(max_length=50)
    d           = models.CharField(max_length=50)

class Term(models.Model):
    term_id         = models.AutoField(primary_key=True)
    spec_point      = models.FloatField()
    term            = models.TextField()
    definition      = models.TextField()