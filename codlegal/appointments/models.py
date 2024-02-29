from django.db import models


# Create your models here.


class PracticeArea(models.Model):
    """
    Model for storing Practice Areas of Advocates
    """
    name = models.CharField(max_length=25, verbose_name='Name of Law')
    description = models.TextField()
