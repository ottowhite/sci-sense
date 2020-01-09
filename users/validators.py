from django.core.exceptions import ValidationError

def password_length_validator(password):
    # checks that the password meets the length requirement
    if len(password) < 8:
        raise ValidationError('Your password be a minimum of 8 characters. ')
    else:
        # otherwise the validator returns the password to the main flow
        return password

def password_contains_capital(password):
    # checks if there exists a True in an iterable where
    # the iterable is a tuple that contains an entry for 
    # every letter, and is True if this letter is uppercase
    if not any(letter.isupper() for letter in password):
        # if there is no uppercase letter present, a validation error is raised
        raise ValidationError('Your password must contain an uppercase character. ')
    else:
        # otherwise the validator returns the password to the main flow
        return password

def password_contains_number(password):
    # checks if there exists a True in an iterable where
    # the iterable is a tuple that contains an entry for 
    # every letter, and is True if this letter is a digit
    if not any(letter.isdigit() for letter in password):
        # if there is no uppercase letter present, a validation error is raised
        raise ValidationError('Your password must contain a number. ')
    else:
        # otherwise the validator returns the password to the main flow
        return password