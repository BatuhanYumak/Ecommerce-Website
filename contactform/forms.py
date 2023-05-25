from django import forms
from contactform.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'message')
