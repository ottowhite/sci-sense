from django.urls import path
from . import views
from main_app.views import GenerateQuizView, QuizView, HomeView

urlpatterns = [
    path('home', HomeView.as_view(), name="main-home"),
    path('quiz', QuizView.as_view(), name="main-quiz"),
    path('generate_quiz', GenerateQuizView.as_view(), name="main-generate-quiz"),
]