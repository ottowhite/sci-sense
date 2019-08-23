from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import AppUser
from .models import Question
from main_app.forms import GenerateQuizForm
from django.db.models import Q, ObjectDoesNotExist
from urllib.parse import urlencode
from django.urls import reverse

# querying the user model
try:
    user_data = AppUser.objects.get(Q(username="britannioj") & Q(password="MLG"))
except ObjectDoesNotExist:
    user_data = None


class HomeView(TemplateView):
    template_name = 'main_app/home.html'


    def get(self, request):
        # this method is called upon the initial request for the webpage
        
        # the args are the different pieces of session/page data that the page will adapt to
        args = {
            'user_data': user_data,
            'title': 'Home'
        }

        # the render method will combine the template with given context, then return generated HttpResponse
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

        # create a form variable on the page containing the filled out post data
        form = GenerateQuizForm(request.POST)

        # defining some arguments to be interacted with on the page
        args = {
            'user_data': user_data,
            'form': form,
            'title': 'Generate quiz'
        }

        # ensuring that the form inputs are valid
        if form.is_valid():
            # retrieving the absolute url of the main quiz page through a reverse lookup based on the
            # name defined on created url patterns
            base_url = reverse('main-quiz')

            # converting a dict containing GET data into a querystring to be used in the quiz page request
            query_string = urlencode({
                'starting_specification_point': form.cleaned_data['starting_specification_point'],
                'ending_specification_point': form.cleaned_data['ending_specification_point'],
                'maximum_questions': form.cleaned_data['maximum_questions']
            })

            # creating a get request with parameters from the form
            return redirect(f'{base_url}?{query_string}')

class QuizView(TemplateView):
    template_name = 'main_app/quiz.html'

    def get(self, request):
        # retrieving the different form values from the address, casting to according data types
        start = float(request.GET.get('starting_specification_point'))
        end = float(request.GET.get('ending_specification_point'))
        maximum = int(request.GET.get('maximum_questions'))

        # swapping the order of the start and end spec position if they 
        # are in the wrong order
        (start, end) = (end, start) if start > end else (start, end)

        # ensuring that there can be no more than 30 questions in a quiz
        maximum = 30 if maximum > 30 else maximum

        # also adds a randomly ordered queryset of given length within the given range, containing questions
        args = {
            'user_data': user_data,
            'question_data': Question.objects.filter(spec_point__range=(start, end)).order_by("?")[:maximum],
            'title': 'Do quiz'
        }

        return render(request, self.template_name, args)