
from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['full_name', 'email', 'phone_number', 'education', 'work_experience', 'skills']
        # Add more fields as needed
