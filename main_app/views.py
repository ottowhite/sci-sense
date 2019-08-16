from django.shortcuts import render
from .models import AppUser
from .models import Question
from django.db.models import Q, ObjectDoesNotExist

# querying the 
try:
    user_data = AppUser.objects.get(Q(username="britannioj") & Q(password="MLG"))
except ObjectDoesNotExist:
    user_data = None


def home(request):
    context = {
        'user_data': user_data,
        'title': 'Home'
    }

    return render(request, 'main_app/home.html', context)

def quiz(request):

    
    context = {
        'user_data': user_data,
        'question_data': Question.objects.filter(spec_point__range=(1.01, 2.1))[:15],
        'title': 'Do quiz'
    }

    return render(request, 'main_app/quiz.html', context)