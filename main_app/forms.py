from django import forms
from main_app.models import Question, Term, Topic

import ipdb

class GenerateQuizForm(forms.Form):
    # this form will be passed as context to the quiz view
    # when referenced with form.as_p, it will be rendered
    # as a paragraph

    # loading all distinct spec points that exist in the database a lists of tuples - (passed value, human readable)
    choices = []
    for topic in Topic.objects.all().order_by("topic_number"):

        # create a specification range from the topic
        # number that has inclusive lower and non inclusive upper
        lower_specification_bound = topic.topic_number
        upper_specification_bound = topic.topic_number + 0.999

        # only display the topic options if there exist questions for them
        if (Question.objects.filter(specification_point__range=(lower_specification_bound, upper_specification_bound)).count() != 0):
            choices.append((topic.topic_number, topic.topic_name))

    topic = forms.ChoiceField(choices=choices)
    maximum_questions = forms.IntegerField()

class GenerateTermsForm(forms.Form):
    # this form will be passed as context to the quiz view
    # when referenced with form.as_p, it will be rendered
    # as a paragraph

    # loading all distinct spec points that exist in the database a lists of tuples - (human readable, passed value)
    
    choices = [(x['specification_point'], x['specification_point']) for x in Term.objects.order_by("specification_point").distinct().values('specification_point')]
    # choices = [(x, x) for x in [1.1, 1.2, 1.3, 1.4]]

    starting_specification_point = forms.ChoiceField(choices=choices)
    ending_specification_point = forms.ChoiceField(choices=choices)
    in_order = forms.BooleanField(required=False)