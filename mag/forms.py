from mag.models import Contact
from django.forms import ModelForm
from django import forms
class ContactForm(ModelForm):
    subject = forms.CharField(required=False,empty_value=None)
    class Meta():
        model = Contact
        fields = ['subject','sender','email','message']
        