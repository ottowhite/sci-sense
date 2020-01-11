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
    # every character, and is True if this character is uppercase
    if not any(character.isupper() for character in password):
        # if there is no uppercase character present, a validation error is raised
        raise ValidationError('Your password must contain an uppercase character. ')
    else:
        # otherwise the validator returns the password to the main flow
        return password

def password_contains_number(password):
    # checks if there exists a True in an iterable where
    # the iterable is a tuple that contains an entry for 
    # every character, and is True if this character is a digit
    if not any(character.isdigit() for character in password):
        # if there is no uppercase character present, a validation error is raised
        raise ValidationError('Your password must contain a number. ')
    else:
        # otherwise the validator returns the password to the main flow
        return password