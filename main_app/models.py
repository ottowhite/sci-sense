from django.db import models
from users import models as users_models

class Question(models.Model):
    # defining the multiple-choice question table with the django ORM

    # EDGE CASE: RANDOMISE THE ORDER WITH WHICH QUESTIONS ARE DISPLAYED
    question_id             = models.AutoField(primary_key=True)
    specification_point     = models.FloatField()
    question                = models.TextField()
    diagram_name            = models.TextField(default='')
    a                       = models.CharField(max_length=50)
    b                       = models.CharField(max_length=50)
    c                       = models.CharField(max_length=50)
    d                       = models.CharField(max_length=50)
    correct_answer          = models.CharField(max_length=1, default='')

class Topic(models.Model):
    topic_id        = models.AutoField(primary_key=True)
    topic_number    = models.IntegerField()
    topic_name      = models.TextField()

class Term(models.Model):

    term_id                 = models.AutoField(primary_key=True)
    specification_point     = models.FloatField()
    term                    = models.TextField()
    definition              = models.TextField()


class SpecReference(models.Model):
    
    topic_number    = models.FloatField(primary_key=True)
    topic_name      = models.TextField()


class Answer(models.Model):

    answer_id       = models.AutoField(primary_key=True)
    user            = models.ForeignKey(users_models.User, on_delete=models.CASCADE) # Foreign key referencing User table
    question        = models.ForeignKey(Question, on_delete=models.CASCADE) # models.CASCADE deletes this entity when referenced entitity is deleted
    answered_on     = models.DateTimeField(auto_now_add=True)
    is_correct      = models.BooleanField()


class Quiz(models.Model):
    
    quiz_id                 = models.AutoField(primary_key=True)
    specification_range     = models.TextField()  # maybe change later
    no_questions            = models.IntegerField()

    def __str__(self):
        return f"specification_range: {self.specification_range}, no_questions: {self.no_questions}"

class QuizResult(models.Model):

    result_id           = models.AutoField(primary_key=True)
    quiz                = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user                = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    percentage_correct  = models.FloatField()
    completed_on        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"specification_range: {self.quiz.specification_range}, no_questions: {self.quiz.no_questions}, correct: {self.percentage_correct}"

class Class(models.Model):

    class_id    = models.AutoField(primary_key=True) 
    class_name  = models.TextField()
    class_owner = models.ForeignKey(users_models.User, on_delete=models.CASCADE)

class ClassMembership(models.Model):

    membership_id   = models.AutoField(primary_key=True)
    user            = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    class_ref       = models.ForeignKey(Class, on_delete=models.CASCADE) # is class_ref as class is a keyword

class Assignment(models.Model):

    assignment_id   = models.AutoField(primary_key=True)
    date_set        = models.DateField()
    date_due        = models.DateField()
    quiz            = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    class_ref       = models.ForeignKey(Class, on_delete=models.CASCADE)