from django.shortcuts import render

user_data = {
    'username': 'robster',
    'forename': 'Robbie',
    'surname': 'McCabe'
}


# Create your views here.
def student_home(request):
    context = {
        'user_data': user_data,
        'title': 'Student home'
    }

    return render(request, 'main_app/student_home.html', context)

def teacher_home(request):
    context = {
        'user_data': user_data,
        'title': 'Teacher home'
    }

    return render(request, 'main_app/teacher_home.html', context)