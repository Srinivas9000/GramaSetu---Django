from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback', 'rating']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'feedback': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your feedback...',
                'rows': 4
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rating (1-5)'
            }),
        }
