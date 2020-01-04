from main_app.models import (
    Question,
    Topic,
    Term,
    Answer,
    Class,
    ClassMembership,
    Assignment,
    Quiz,
    QuizResult
)

Question.objects.all().delete()
Term.objects.all().delete()
Class.objects.all().delete()
QuizResult.objects.all().delete()
Quiz.objects.all().delete()
Assignment.objects.all().delete()
ClassMembership.objects.all().delete()
Answer.objects.all().delete()