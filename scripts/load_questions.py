import pandas as pd
from main_app.models import Question
import ipdb


questions = pd.read_csv('scripts/question_data/data.csv')
relevant = questions[["Spec", "Question", "A", "B", "C", "D", "Answer"]]

question_list = []

for i in range(len(relevant)):
    spec_point, question, a, b, c, d, answer = relevant.iloc[i].values

    question_list.append(Question(spec_point=spec_point, question=question, a=a, b=b, c=c, d=d, answer=answer))

#Question.objects.bulk_create(question_list)