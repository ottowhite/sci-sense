import os
import ipdb
import re
import pandas as pd

def rename():
    path = 'physics_diagrams'
    files = os.listdir(path)

    for x in range(len(files)):
        print(files[x])
        new_filename = re.sub('^(Spec )', '', files[x])
        print(new_filename)

        os.rename(f"{path}/{files[x]}", f"{path}/{new_filename}")

def create_references():
    diagram_path = 'physics_diagrams'
    diagram_names = os.listdir(diagram_path)
    questions_path = 'question_data/question_data.csv'
    
    questions = pd.read_csv(questions_path, index_col=0)

    for x in range(len(questions)):
        if (questions['diagram_name'].iloc[x] == 'Y'):
            for y in range(len(diagram_names)):
                if (float(questions['specification_point'].iloc[x]) == float(diagram_names[y][:4])):
                    print(questions['specification_point'].iloc[x], diagram_names[y][:4])

                    questions['diagram_name'].iloc[x] = diagram_names[y]

    print(questions)
    ipdb.set_trace()


create_references()
