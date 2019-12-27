import pandas as pd
import ipdb

data = pd.read_csv('question_data/data.csv')

print(f"INCORRECT TABLE: \n\n{data.head()}\n\n")

pd.set_option('mode.chained_assignment', None)
for x in range(len(data)):
    # get the answer letter and according answer
    answer_letter = data.iloc[x]['Answer']
    answer = data.iloc[x][answer_letter]

    # move the answer into the A column
    if (answer_letter == 'A'):
        pass
    else:
        temp = data['A'].iloc[x]
        data['A'].iloc[x] = data.iloc[x][answer_letter]
        data[answer_letter].iloc[x] = temp

print(f"CORRECT TABLE: \n\n{data.head()}\n\n")

data = data.drop(columns=['Answer', 'Spec Text', 'T/P/*'])
data = data.rename(columns={'Diagram':'diagram_name', 'Spec':'specification_point', 'Question':'question', 'A':'a', 'B':'b', 'C':'c', 'D':'d'})

print(data.head())

data.to_csv('question_data/data.csv')