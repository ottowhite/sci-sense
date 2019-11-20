import pandas as pd
from main_app.models import Question, Term
import numpy as np
import ipdb

csv_path = 'scripts/question_data/data.csv'

def import_questions(csv_path):
    questions = pd.read_csv(csv_path)

    relevant = questions[["Spec", "Question", "Diagram", "A", "B", "C", "D", "Answer"]]

    # Convert the Diagram column from 'Y' or NaN to True or False
    relevant['Diagram'] = relevant['Diagram'].map(lambda x: True if x == 'Y' else False)

    question_list = []

    for i in range(len(relevant)):
        spec_point, question, diagram, a, b, c, d, answer = relevant.iloc[i].values

        question_list.append(Question(spec_point=spec_point, question=question, diagram=diagram, a=a, b=b, c=c, d=d, answer=answer))

    ipdb.set_trace()
    Question.objects.bulk_create(question_list)

def import_terms_temp():
    
    term_list = []
    for x in range(11, 80):
        spec_point = x / 10
        term = "This is a term"
        definition = "This is a definition"

        term_list.append(Term(spec_point=spec_point, term=term, definition=definition))

    ipdb.set_trace()
    Term.objects.bulk_create(term_list)


