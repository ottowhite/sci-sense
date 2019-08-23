from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from main_app.views import GenerateQuizView, QuizView, HomeView

urlpatterns = [
    path('', RedirectView.as_view(url='/home'), name='main'),
    path('home', HomeView.as_view(), name="main-home"),
    path('quiz', QuizView.as_view(), name="main-quiz"),
    path('generate_quiz', GenerateQuizView.as_view(), name="main-generate-quiz"),
]