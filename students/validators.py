from django.core.exceptions import ValidationError


def validate_unique_email(value):
    from students.models import Student

    email_list = Student.objects.values_list('email', flat=True)
    if value in email_list:
        raise ValidationError('This email already is in database')
