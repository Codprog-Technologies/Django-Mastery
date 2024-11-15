from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import User


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
        verbose_name = _("Practice Area")
        verbose_name_plural = _("Practice Areas")
        db_table = "appointments_practicearea"
        constraints = [
            models.UniqueConstraint(name="pa_name_unq", fields=('name',)),
        ]


class Appointment(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="+",
                               limit_choices_to={'role': User.RoleChoices.CLIENT})
    advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="+",
                                 limit_choices_to={'role': User.RoleChoices.ADVOCATE})
    start_at = models.DateTimeField(_("Start At"))
    created_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.start_at < timezone.now():
            raise ValidationError({'start_at': 'Start Time should be of Future.'})
