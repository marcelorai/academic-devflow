from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date_is_today_or_after(value):
    today = timezone.now().date()
    if (today > value):
        raise ValidationError('A data é anterior a hoje')
