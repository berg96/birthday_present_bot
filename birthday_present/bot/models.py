from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class TelegramUser(models.Model):
    user_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


def validate_not_future_date(value):
    if value > timezone.now().date():
        raise ValidationError("Дата не может быть в будущем.")


class Friend(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(validators=[validate_not_future_date])
    user = models.ForeignKey(
        TelegramUser, related_name='friends', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Gift(models.Model):
    friend = models.ManyToManyField(Friend, related_name='gifts', null=True)
    present = models.CharField(max_length=100)

    def __str__(self):
        return self.present
