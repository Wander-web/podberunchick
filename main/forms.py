from django import forms
from django.contrib.auth.models import User
from main import models


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['title', 'code', 'description',
                  'tag_1', 'tag_2', 'tag_3']

        widgets = {'description': forms.Textarea(attrs={"rows": 3, "cols": 10})}
