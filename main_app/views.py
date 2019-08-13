from django.shortcuts import render
from django.contrib.auth.models import User

user_data = {
    'username': 'robster',
    'forename': 'Robbie',
    'surname': 'McCabe'
}


# Create your views here.
def student_home(request):
    context = {
        'user_data': User.objects.get(username="ottowhite"),
        'title': 'Student home'
    }

    return render(request, 'main_app/student_home.html', context)

def teacher_home(request):
    context = {
        'user_data': User.objects.get(username="ottowhite"),
        'title': 'Teacher home'
    }

    return render(request, 'main_app/teacher_home.html', context)

def student_quiz(request):
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
        'user_data': User.objects.first(),
        'question_data': question_data,
        'title': 'Do quiz'
    }

    return render(request, 'main_app/student_quiz.html', context)