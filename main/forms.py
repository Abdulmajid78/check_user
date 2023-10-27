from django import forms
from .models import ContactMessageModel
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessageModel
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
                'data-error': "Please enter your name",
                'required': 'True'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your email',
                'type': 'email',
                'class': 'form-control',
                'data-error': "Please enter your email",
                'required': 'True'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'phone number',
                'type': 'number',
                'class': 'form-control',
                'data-error': "Please enter your number",
                'required': 'True'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Your Subject',
                'class': 'form-control',
                'data-error': "Please enter your subject",
                'required': 'True'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Write Message',
                'class': 'form-control message-field',
                'data-error': "Please type your message",
                'required': 'True',
                'cols': "30",
                'rows': "7"
            }),

        }
