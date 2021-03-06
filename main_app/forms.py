from django import forms
from main_app.models import Question, Term, Topic
from main_app.validators import number_of_questions_validator

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

        # if querying the specification range of a particular topic returns items
        if (Question.objects.filter(specification_point__range=(lower_specification_bound, upper_specification_bound)).count() != 0):
            # append this topic name and number of the choices displayed on the topic name field
            choices.append((topic.topic_number, topic.topic_name))

    # display this list of topics as a dropdown consisting of only the topics
    topic = forms.ChoiceField(choices=choices)
    maximum_questions = forms.IntegerField(validators=[number_of_questions_validator])

class GenerateTermsForm(forms.Form):
    # this form will be passed as context to the quiz view
    # when referenced with form.as_p, it will be rendered
    # as a paragraph
    choices = []
    for topic in Topic.objects.all().order_by("topic_number"):

        # create a specification range from the topic
        # number that has inclusive lower and non inclusive upper
        lower_specification_bound = topic.topic_number
        upper_specification_bound = topic.topic_number + 0.999

        # only display the topic options if there exist questions for them
        if (Term.objects.filter(specification_point__range=(lower_specification_bound, upper_specification_bound)).count() != 0):
            choices.append((topic.topic_number, topic.topic_name))

    topic = forms.ChoiceField(choices=choices)
    in_order = forms.BooleanField(required=False)

class UploadQuestionsForm(forms.Form):

    questions_csv = forms.FileField(required=True, label='Filled template')