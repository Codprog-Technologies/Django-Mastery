from django import forms

from reviews import models


class PlatformReviewForm(forms.ModelForm):
    class Meta:
        model = models.PlatformReview
        exclude = ["user"]
