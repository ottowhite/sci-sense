import pandas as pd
from main_app.models import Question, Term, Topic
import numpy as np
import ipdb
import random

def import_questions(path):
    questions = pd.read_csv(path, index_col=0)

    question_list = []

    for x in range(len(questions)):
        answers = [None] * 4
        specification_point, diagram_name, question, answers[0], answers[1], answers[2], answers[3] = questions.iloc[x].values
        
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

def import_terms(path):
    terms = pd.read_csv(path, index_col=0)

    term_list = []

    for x in range(len(terms)):
        term_list.append(Term(
            specification_point=terms.values[x][0],
            term=terms.values[x][1],
            definition=terms.values[x][2]))

    Term.objects.bulk_create(term_list)

def import_topics(path):
    topics = pd.read_csv(path, index_col=0)

    topic_list = []

    for x in range(len(topics)):
        topic_list.append(Topic(
            topic_number=topics.values[x][0],
            topic_name=topics.values[x][1]))

    Topic.objects.bulk_create(topic_list)

import_topics('scripts/question_data/topic_data.csv')


