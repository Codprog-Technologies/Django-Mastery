from django import forms

from appointments import models


class PracticeAreaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for bound_field in self.visible_fields():
            if bound_field.field.widget.attrs.get('class'):
                bound_field.field.widget.attrs['class'] += ' form-control'
            else:
                bound_field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.PracticeArea
        fields = ('name', 'description')  # __all__

        # widgets = {
        #     'name': forms.TextInput(attrs={"class": "form-control"}),
        #     'description': forms.Textarea(attrs={"class": "form-control"})
        # }