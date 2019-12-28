import pandas as pd
from main_app.models import Question, Term
import numpy as np
import ipdb

def import_questions(path):
    questions = pd.read_csv(path, index_col=0)

    question_list = []

    for x in range(len(questions)):
        specification_point, diagram_name, question, a, b, c, d = questions.iloc[x].values

        question_list.append(Question(
            specification_point=specification_point, 
            question=question, 
            diagram_name=diagram_name, 
            a=a, 
            b=b, 
            c=c, 
            d=d))
        

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

import_questions('scripts/question_data/question_data.csv')
import_terms('scripts/question_data/term_data.csv')


