import pandas as pd
import ipdb
from io import StringIO
from main_app.models import Question
from django.contrib import messages
import random
import math

def upload_questions(request):
    # retrieving the csv file from the request
    questions_csv = request.FILES['questions_csv'].read()

    
    questions_dataframe = pd.read_csv(                          # reading the file to a pandas dataframe for manipulation
        StringIO(                                               # casting to a StringIO format as pd.read_csv can use this
            questions_csv.decode('utf-8').replace('\r', '')))   # decoding the text encoding and removing unnecessary characters

    # passing the unvalidated dataframe to the categorise questions function
    # and using the returned categorised Question object lists
    questions_dict = categorise_questions(questions_dataframe)

    # totalling the different categorisations
    incomplete_count = len(questions_dict['incomplete_questions'])
    valid_count = len(questions_dict['valid_questions'])
    existing_count = len(questions_dict['already_existing'])
    total_questions = incomplete_count + valid_count + existing_count

    # ----------- Adding any messages to the request if necessary ------------------
    if len(questions_dict['incomplete_questions']) != 0:
        messages.add_message(request, messages.WARNING, f'{incomplete_count} of {total_questions} questions have incomplete data.')
    
    if len(questions_dict['already_existing']) != 0:
        messages.add_message(request, messages.WARNING, f'{existing_count} of {total_questions} already exist in the database')
    
    if len(questions_dict['valid_questions']) != 0:
        messages.add_message(request, messages.WARNING, f'{valid_count} of {total_questions} are to be uploaded.')
    else:
        messages.add_message(request, messages.WARNING, f'There exist no valid questions to be uploaded.')
    # ----------- These messages will be displayed on the upload questions page ------------------

    # uploading valid questions if they exist, otherwise doing nothing
    Question.objects.bulk_create(questions_dict['valid_questions']) if valid_count != 0 else False

def categorise_questions(questions_dataframe):
    # the answers array is overwritten at every iteration
    # and only must exist temporarily
    answers = [None] * 4

    # stores all different categorisations of questions
    questions_dict = {
        'valid_questions': [],
        'incomplete_questions': [],
        'already_existing': []
    }

    # iterating over the unvalidated questions dataframe
    for x in range(len(questions_dataframe)):
        # unpack the values from the dataframe into variables and an answers array
        specification_point, diagram_name, question, answers[0], answers[1], answers[2], answers[3] = questions_dataframe.iloc[x].values

        # creating an array to be iterated over when checking for unpopulated required fields
        required_fields = [specification_point, question, answers[0], answers[1], answers[2], answers[3]]

        correct_answer = answers[0] # retrieving the correct answer string
        random.shuffle(answers) # randomising the order of the answers
        # finding index of correct answer, and convert {0, 1, 2, 3} into {a, b, c, d}
        correct_answer_letter = chr(answers.index(correct_answer) + 97) 

        if any(str(field) == 'nan' for field in required_fields):
            # checking whether required fields are unpopulated
            # if they are, populating and appending a question object to a 
            # list of incomplete questions in the questions dict
            questions_dict['incomplete_questions'].append(Question(
                specification_point=specification_point, 
                question=question, 
                diagram_name=diagram_name, 
                a=answers[0], 
                b=answers[1], 
                c=answers[2], 
                d=answers[3],
                correct_answer=correct_answer_letter))

        elif Question.objects.filter(question=question).count() != 0:
            # checking whether a question already exists in the database
            # if it does, populating and appending the question object to a 
            # list of existing questions in the questions dict
            questions_dict['already_existing'].append(Question(
                specification_point=specification_point, 
                question=question, 
                diagram_name=diagram_name, 
                a=answers[0], 
                b=answers[1], 
                c=answers[2], 
                d=answers[3],
                correct_answer=correct_answer_letter))
        else:
            # otherwise these questions will be valid
            # thus they are appended to a list of valid questions
            questions_dict['valid_questions'].append(Question(
                specification_point=specification_point, 
                question=question, 
                diagram_name=diagram_name, 
                a=answers[0], 
                b=answers[1], 
                c=answers[2], 
                d=answers[3],
                correct_answer=correct_answer_letter))

    return questions_dict