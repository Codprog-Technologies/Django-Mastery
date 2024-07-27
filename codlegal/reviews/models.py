from django.conf import settings
from django.db import models


# Create your models here.


class PlatformReview(models.Model):
    class SatisfactionChoices(models.IntegerChoices):
        VERY_SATISFIED = 5, 'Very Satisfied'
        SATISFIED = 4, 'Satisfied'
        NEUTRAL = 3, 'Neutral'
        UNSATISFIED = 2, 'Unsatisfied'
        VERY_UNSATISFIED = 1, 'Very Unsatisfied'

    satisfaction = models.PositiveSmallIntegerField("How satisfied are you with our Platform?", choices=SatisfactionChoices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
