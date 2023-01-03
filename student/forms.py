from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['students_number','first_name','last_name','email','field_of_study','gpa']
        labels = {
            'students_number':'Student Number',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'field_of_study':'Field of Study',
            'gpa':'GPA',
        }
        widgets = {
            'students_number': forms.NumberInput(attrs={'class': 'form-comtrol'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-comtrol'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-comtrol'}),
            'email' : forms.EmailInput(attrs={'class': 'form-comtrol'}),
            'field_of_study' : forms.TextInput(attrs={'class': 'form-comtrol'}),
            'gpa' : forms.NumberInput(attrs={'class': 'form-comtrol'}),
        }