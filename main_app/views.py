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
    
    # a queryset of 15 randomly ordered question objects from a range in the spec is passed
    context = {
        'user_data': user_data,
        'question_data': Question.objects.filter(spec_point__range=(1.2, 1.3)).order_by("?")[:3],
        'title': 'Do quiz'
    }

    return render(request, 'main_app/quiz.html', context)