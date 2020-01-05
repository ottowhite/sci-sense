from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.models import ObjectDoesNotExist, Case, When, Q
from urllib.parse import urlencode
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import ipdb

from main_app.models import (
    Question, 
    Answer, 
    Quiz, 
    QuizResult, 
    Topic, 
    Term
)

from main_app.forms import (
    GenerateQuizForm, 
    GenerateTermsForm, 
    UploadQuestionsForm
)

class LoginRequiredTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'


class HomeView(LoginRequiredTemplateView):
    template_name = 'main_app/home.html'


    def get(self, request):
        # this method is called upon the initial request for the webpage
        
        # the args are the different pieces of session/page data that the page will adapt to
        args = {
            'title': 'Home'
        }

        # the render method will combine the template with given context, then return generated HttpResponse
        return render(request, self.template_name, args)


class GenerateQuizView(LoginRequiredTemplateView):
    template_name = 'main_app/generate_quiz.html'

    def get(self, request):
        # This method handles the GET request upon intially viewing the page

        # create a new form for the page
        form = GenerateQuizForm()

        # defining some arguments to be interacted with on the page
        args = {
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
            'form': form,
            'title': 'Generate quiz'
        }
        
        # ensuring that the form inputs are valid
        if form.is_valid():

            request.session['starting_specification_point'] = float(form.cleaned_data['topic'])
            request.session['ending_specification_point']   = float(form.cleaned_data['topic']) + 0.999
            request.session['maximum_questions']            = int(form.cleaned_data['maximum_questions'])
            request.session['quiz_name'] = Topic.objects.get(topic_number=int(form.cleaned_data['topic'])).topic_name

            # creating a get request with parameters from the form
            return redirect('main-quiz')
        
        else:

            return redirect('main-generate-quiz')


class GenerateTermsView(LoginRequiredTemplateView):
    template_name = 'main_app/generate_terms.html'


    def get(self, request):
        # This method handles the GET request upon intially viewing the page

        # create a new form for the page
        form = GenerateTermsForm()

        # defining some arguments to be interacted with on the page
        args = {
            'form': form,
            'title': 'Display terms and definitions'
        }

        # render the page with the according context
        return render(request, self.template_name, args)


    def post(self, request):
        # This method handles the GET request upon intially viewing the page

        # create a form variable on the page containing the filled out post data
        form = GenerateTermsForm(request.POST)

        # defining some arguments to be interacted with on the page
        args = {
            'form': form,
            'title': 'Terms and Definitions'
        }
        
        # ensuring that the form inputs are valid
        if form.is_valid():

            request.session['starting_specification_point'] = float(form.cleaned_data['topic'])
            request.session['ending_specification_point']   = float(form.cleaned_data['topic']) + 0.999
            request.session['in_order']                     = bool(form.cleaned_data['in_order'])

            # creating a get request with parameters from the form
            return redirect('main-terms')
        
        else:

            return redirect('main-generate-terms')


class QuizView(LoginRequiredTemplateView):
    template_name = 'main_app/quiz.html'


    def get(self, request):
        
        try:
            # retrieving the different form values from the address, casting to according data types
            start   = request.session['starting_specification_point']
            end     = request.session['ending_specification_point']
            maximum = request.session['maximum_questions']

            # swapping the order of the start and end spec position if they 
            # are in the wrong order
            (start, end) = (end, start) if start > end else (start, end)

            # ensuring that there can be no more than 30 questions in a quiz, and that numbers below 1 give a max of 10
            if maximum > 30:
                maximum = 30
            elif maximum < 1:
                maximum = 10

            # also adds a randomly ordered queryset of given length within the given range, containing questions
            args = {
                'question_data': Question.objects.filter(specification_point__range=(start, end)).order_by("?")[:maximum],
                'title': 'Do quiz'
            }

            return render(request, self.template_name, args)

        except KeyError:
            # In the event that the retrieving part of the GET request query string
            # results in a type error as is empty, redirect to the quiz generation page
            return redirect('main-generate-quiz')


    def post(self, request):
        # temporarily store the answers in a User variable in the database  MAKE ME BETTER      
        current_user = request.user
        answers = json.loads(request.POST['answers'])
        answer_objects = []
        correct_answers = 0
        smallest_spec = 100
        largest_spec = 0
        
        # Collecting correct answers and adding Answer objects
        for x in answers:
            current_question_object = Question.objects.get(question_id=x[1])

            # append the correct answer to the row, convert {a, b, c, d} to {1, 2, 3, 4}
            x.append(ord(current_question_object.correct_answer) - 96)

            # check if the user answer matches the retrieved answer
            if (x[2] == x[3]):
                is_correct = True
                correct_answers += 1
            else:
                is_correct = False
            
            if (current_question_object.specification_point > largest_spec):
                largest_spec = current_question_object.specification_point
            if (current_question_object.specification_point < smallest_spec):
                smallest_spec = current_question_object.specification_point

            
            answer_objects.append(Answer(
                user            = current_user,
                question        = Question.objects.get(question_id=x[1]),
                is_correct      = is_correct
            ))

        Answer.objects.bulk_create(answer_objects)

        specification_range = f"[{smallest_spec}, {largest_spec}]"
        no_questions = len(answers)

        # Either get the existing quiz or create a new one if not exists
        if not Quiz.objects.filter(Q(specification_range=specification_range) & Q(no_questions=no_questions)):
            quiz = Quiz(
                specification_range=specification_range, 
                no_questions=no_questions,
                quiz_name=request.session['quiz_name'])
            quiz.save()

        else:
            quiz = Quiz.objects.filter(Q(specification_range=specification_range) & Q(no_questions=no_questions)).first()

        # creating the quizResult object
        percentage_correct = round(((correct_answers / no_questions) * 100), 1)

        quiz_result = QuizResult(
            quiz=quiz,
            user=current_user,
            percentage_correct=percentage_correct
        )

        quiz_result.save()

        request.session['last_quiz'] = answers

        # remove the session variables that allow the quiz to be backtracked to
        request.session.pop('starting_specification_point', None)
        request.session.pop('ending_specification_point', None)
        request.session.pop('maximum_questions', None)
        request.session.pop('quiz_name', None)

        return redirect('main-review-quiz')


class TermsView(LoginRequiredTemplateView):
    template_name = 'main_app/terms.html'

    

    def get(self, request):
        try:
            # retrieving the different form values from the address, casting to according data types
            start    = request.session['starting_specification_point']
            end      = request.session['ending_specification_point']
            in_order = request.session['in_order']

            # swapping the order of the start and end spec position if they 
            # are in the wrong order
            (start, end) = (end, start) if start > end else (start, end)

            if in_order == True:
                terms = Term.objects.filter(specification_point__range=(start, end))
            else:
                terms = Term.objects.filter(specification_point__range=(start, end)).order_by('?')
            
            args = {
                'terms': terms,
                'title': 'Terms and definitions'
            }

            return render(request, self.template_name, args)
        except KeyError:
            return redirect('main-generate-terms')


class ReviewQuizView(LoginRequiredTemplateView):
    template_name = 'main_app/review_quiz.html'


    def get(self, request):
        try:
            # also adds a randomly ordered queryset of given length within the given range, containing questions
            last_quiz = eval(str(request.session['last_quiz'])) # evaluates the JSON last quiz state
            question_ids = [x[1] for x in last_quiz] # retrieves the question ids 
            
            # Creates a set of conditions that places question in according place
            preserved = Case(*[When(question_id=question_id, then=index) for index, question_id in enumerate(question_ids)])

            question_data = Question.objects.filter(question_id__in=question_ids).order_by(preserved)

            args = {
                'question_data': question_data,
                'title': 'Do quiz',
            }

            return render(request, self.template_name, args)
        except KeyError:
            return redirect('main-generate-quiz')


class ViewResultsView(LoginRequiredTemplateView):
    template_name = 'main_app/view_results.html'

    def get(self, request):
        current_user = request.user

        args = {
            'title': 'My Results',
            'results': QuizResult.objects.filter(user=current_user).order_by('-completed_on')
        }

        return render(request, self.template_name, args)


class ManageQuestionsView(LoginRequiredTemplateView):
    template_name = 'main_app/manage_questions.html'

    def get(self, request):
        
        form = UploadQuestionsForm()

        args = {
            'title': 'Manage questions',
            'form': form
        }

        return render(request, self.template_name, args)
    
    def post(self, request):
        form = UploadQuestionsForm(request.POST, request.FILES)

        if form.is_valid():
            print(request.FILES['questions_csv'].read())
        
        args = {
            'title': 'Manage questions',
            'form': form
        }

        return render(request, self.template_name, args)