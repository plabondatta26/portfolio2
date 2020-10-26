from django import forms
from .models import GetInTouch


class EmailForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ['name', 'email_address', 'subject', 'message', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email_address': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Email subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write message'}),
        }

