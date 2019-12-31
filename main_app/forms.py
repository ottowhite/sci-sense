from django import forms
from main_app.models import Question, Term, Topic

import ipdb

class GenerateQuizForm(forms.Form):
    # this form will be passed as context to the quiz view
    # when referenced with form.as_p, it will be rendered
    # as a paragraph

    # loading all distinct spec points that exist in the database a lists of tuples - (human readable, passed value)
    choices = [(x.topic_number, x.topic_name) for x in Topic.objects.all().order_by("topic_number")]

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