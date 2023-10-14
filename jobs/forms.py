from django import forms
from .models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['employee', 'created_at', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'comment': forms.Textarea(attrs={'placeholder': 'comment'}),
        }
