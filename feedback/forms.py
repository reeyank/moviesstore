from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name (Optional)', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Your thoughts on the checkout process', 'class': 'form-control'}),
        }
