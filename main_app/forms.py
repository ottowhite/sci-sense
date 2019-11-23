from django import forms
from main_app.models import Question, Term

import ipdb

class GenerateQuizForm(forms.Form):
    # this form will be passed as context to the quiz view
    # when referenced with form.as_p, it will be rendered
    # as a paragraph

    # loading all distinct spec points that exist in the database a lists of tuples - (human readable, passed value)
    
    choices = [(x['spec_point'], x['spec_point']) for x in Question.objects.order_by("spec_point").distinct().values('spec_point')]

    starting_specification_point = forms.ChoiceField(choices=choices)
    ending_specification_point = forms.ChoiceField(choices=choices)
    maximum_questions = forms.IntegerField()

class GenerateTermsForm(forms.Form):
    # this form will be passed as context to the quiz view
    # when referenced with form.as_p, it will be rendered
    # as a paragraph

    # loading all distinct spec points that exist in the database a lists of tuples - (human readable, passed value)
    
    choices = [(x['spec_point'], x['spec_point']) for x in Term.objects.order_by("spec_point").distinct().values('spec_point')]


    starting_specification_point = forms.ChoiceField(choices=choices)
    ending_specification_point = forms.ChoiceField(choices=choices)
    in_order = forms.BooleanField(required=False)