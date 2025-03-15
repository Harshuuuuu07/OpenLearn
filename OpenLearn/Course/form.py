from django import forms
from .models import course

class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ['title', 'Link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'Link': forms.TextInput(attrs={'class': 'form-control'}),

        }