from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AppUser
from .models import Question
from main_app.forms import GenerateQuizForm
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

class HomeView(TemplateView):
    template_name = 'main_app/home.html'


    def get(self, request):
        args = {
            'user_data': user_data,
            'title': 'Home'
        }

        return render(request, self.template_name, args)

class QuizView(TemplateView):
    template_name = 'main_app/quiz.html'

    def get(self, request):
        args = {
            'user_data': user_data,
            'question_data': Question.objects.filter(spec_point__range=(1.2, 1.3)).order_by("?")[:3],
            'title': 'Do quiz'
        }

        return render(request, self.template_name, args)

class GenerateQuizView(TemplateView):
    template_name = 'main_app/generate_quiz.html'

    def get(self, request):
        # This method handles the GET request upon intially viewing the page

        # create a new form for the page
        form = GenerateQuizForm()

        # defining some arguments to be interacted with on the page
        args = {
            'user_data': user_data,
            'form': form,
            'title': 'Generate quiz'
        }

        # render the page with the according context
        return render(request, self.template_name, args)
    
    def post(self, request):
        # This method handles the GET request upon intially viewing the page

        # create a form on the page containing the post data
        form = GenerateQuizForm(request.POST)

        # defining some arguments to be interacted with on the page
        args = {
            'user_data': user_data,
            'form': form,
            'title': 'Generate quiz'
        }

        if form.is_valid():
            starting_specification_point = form.cleaned_data['starting_specification_point']
            ending_specification_point = form.cleaned_data['ending_specification_point']
            maximum_questions = form.cleaned_data['maximum_questions']
        
        args['values'] = starting_specification_point + ending_specification_point + maximum_questions

        # render the page with the according context
        return render(request, self.template_name, args)