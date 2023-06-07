from django import forms
from contactform.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }