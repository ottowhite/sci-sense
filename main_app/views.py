from django.shortcuts import render
from .models import AppUser

user_data = {
    'username': 'robster',
    'forename': 'Robbie',
    'surname': 'McCabe'
}


# Create your views here.
def home(request):
    context = {
        'user_data': AppUser.objects.get(username="ottowhite"),
        'title': 'Home'
    }

    return render(request, 'main_app/home.html', context)

def quiz(request):
    question_data = {
        'spec_point': '3.12',
        'question': 'What is the base unit of mass?',
        'a': 'Kilograms',
        'b': 'Grams',
        'c': 'Hertz',
        'd': 'Draws',
        'answer': 'd'
    }
    
    context = {
        'user_data': AppUser.objects.get(username="ottowhite"),
        'question_data': question_data,
        'title': 'Do quiz'
    }

    return render(request, 'main_app/quiz.html', context)