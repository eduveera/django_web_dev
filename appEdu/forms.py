# appEdu/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'dob', 'email']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
