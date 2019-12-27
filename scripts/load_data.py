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
    # Question.objects.bulk_create(question_list)

def import_terms_temp():
    
    term_list = []
    for x in range(11, 80):
        spec_point = x / 10
        term = "This is a term"
        definition = "This is a definition"

        term_list.append(Term(spec_point=spec_point, term=term, definition=definition))

    ipdb.set_trace()
    Term.objects.bulk_create(term_list)

def import_terms(csv_path):
    terms = pd.read_csv(csv_path, encoding='ISO-8859-1', header=None, names=['spec_point', 'term', 'definition'])

    terms['term'] = terms.iloc[0:-1:2]
    terms['definition'] = terms.iloc[1:-2:2]
    terms['definition'] = terms['definition'].shift(-1)

    terms['spec_point'] = 0

    terms = terms.dropna()
    terms = terms.reset_index(drop=True)

    terms['spec_point'] = ((terms.index+1) % 100) / 10
    terms['spec_point'] += 1

    term_list = []

    for x in range(len(terms.values)):
        term_list.append(Term(spec_point=terms.values[x][0], term=terms.values[x][1], definition=terms.values[x][2]))

    terms = terms.rename(columns={'spec_point':'specification_point'})

    ipdb.set_trace()
    # Term.objects.bulk_create(term_list)

import_terms('scripts/terms.csv')


