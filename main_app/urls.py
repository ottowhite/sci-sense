from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="main-home"),
    path('quiz', views.quiz, name="main-quiz"),
]