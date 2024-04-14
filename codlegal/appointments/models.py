from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class PracticeArea(models.Model):
    """
    Model for storing Practice Areas of Advocates
    """
    name = models.CharField(max_length=25, verbose_name='Name of Law')
    description = models.TextField()

    def __str__(self):
        return self.name

    def clean(self):
        name = self.name  # different from form.
        # if name == 'Test123':
        #     raise ValidationError({'name': 'This name is not allowed'})

    class Meta:
        verbose_name = "Practice Area"
        verbose_name_plural = "Practice Areas"
        db_table = "appointments_practicearea"
        constraints = [
            models.UniqueConstraint(name="pa_name_unq", fields=('name',)),
        ]
