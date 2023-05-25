from django import forms
from contactform.models import ContactForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')
