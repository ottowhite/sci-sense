from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from main_app.views import GenerateQuizView, QuizView, HomeView, ReviewQuizView, GenerateTermsView, TermsView

urlpatterns = [
    path('', RedirectView.as_view(url='/home'), name='main'),
    path('home', HomeView.as_view(), name="main-home"),
    path('quiz', QuizView.as_view(), name="main-quiz"),
    path('terms', TermsView.as_view(), name="main-terms"),
    path('generate_quiz', GenerateQuizView.as_view(), name="main-generate-quiz"),
    path('generate_terms', GenerateTermsView.as_view(), name="main-generate-terms"),
    path('review_quiz', ReviewQuizView.as_view(), name="main-review-quiz"),
]