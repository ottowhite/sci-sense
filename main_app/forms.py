from django import forms

class GenerateQuizForm(forms.Form):
    starting_specification_point = forms.FloatField()
    ending_specification_point = forms.FloatField()
    maximum_questions = forms.IntegerField()
