from django.core.exceptions import ValidationError

def number_of_questions_validator(number):
    
    # Ensure that the number of questions requested for the quiz is within a
    # suitable range
    if number > 30 or number < 10:
        # if it is not raise a validation error with a message to be displayed
        # on the form when the template is regenerated by the POST request
        raise ValidationError('Quizzes must be between 10 and 30 questions. ')
    else:
        # otherwise return the number to confirm abidande of rules
        return number