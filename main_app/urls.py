from django.urls import path
from . import views

urlpatterns = [
    path('student_home', views.student_home, name="main-student-home"),
    path('teacher_home', views.teacher_home, name="main-teacher-home"),
    path('student_quiz', views.student_quiz, name="main-student-quiz"),
]
