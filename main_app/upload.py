import pandas as pd
import ipdb
from io import StringIO
from main_app.models import Question
from django.contrib import messages
import random

def attempt_upload_questions(request):
    questions_csv = request.FILES['questions_csv'].read()
    current_user = request.user
    questions = pd.read_csv(StringIO(questions_csv.decode('utf-8').replace('\r', '')))

    # messages.add_message(request, messages.WARNING, 'blah')
    # messages.add_message(request, messages.INFO, 'blah')

    upload_questions(questions) if validate_questions(questions) else False

def upload_questions(questions_dataframe):
    question_list = []
    requires_diagram = []

    for x in range(len(questions_dataframe)):
        answers = [None] * 4
        specification_point, diagram_name, question, answers[0], answers[1], answers[2], answers[3] = questions_dataframe.iloc[x].values
        
        correct_answer = answers[0]

        random.shuffle(answers)

        # find index of correct answer, and convert {0, 1, 2, 3} into {a, b, c, d}
        correct_answer_letter = chr(answers.index(correct_answer) + 97)

        question_list.append(Question(
            specification_point=specification_point, 
            question=question, 
            diagram_name=diagram_name, 
            a=answers[0], 
            b=answers[1], 
            c=answers[2], 
            d=answers[3],
            correct_answer=correct_answer_letter))
        
    Question.objects.bulk_create(question_list)

def validate_questions(questions_dataframe):
    # all validation checks will go here
    return True