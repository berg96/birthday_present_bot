from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


def validate_not_future_date(value):
    if value > timezone.now().date():
        raise ValidationError("Дата не может быть в будущем.")


class Friend(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateField(validators=[validate_not_future_date])
    presents = models.ArrayField(models.CharField(max_length=100), null=True)
    user = models.ForeignKey(
        User, related_name='friends', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
