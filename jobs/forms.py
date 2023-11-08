from django import forms
from .models import Comment, EmployeeModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        exclude = ['employee', 'created_at', 'active']
        widgets = {

            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'position': forms.TextInput(attrs={'placeholder': 'Position', 'class': 'form-control'}),
            'employ_from': forms.DateInput(attrs={'placeholder': 'employ_from', 'class': 'form-control', 'type': 'date'}),
            'employ_to': forms.TextInput(attrs={'placeholder': 'employ_to', 'class': 'form-control', 'type': 'date'}),
            'content': forms.TextInput(attrs={'placeholder': 'content', 'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     if 'user' in self.fields:
    #         self.fields['user'].widget = forms.HiddenInput()



class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ('first_name', 'last_name', 'third_name', 'phone_number', 'about', 'experience', 'born_city', 'current_city', 'born_date')



# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = CommentModel
#         # fields = ('position', 'employ_from', 'employ_to', 'content')
#         exclude = ['created_at', 'employee', 'user']
#         widgets = {
#             'position': forms.TextInput(attrs={'placeholder': 'Position', 'class': 'form-control'}),
#             'employ_from': forms.DateInput(attrs={'placeholder': 'employ_from', 'class': 'form-control', 'type': 'date'}),
#             'employ_to': forms.TextInput(attrs={'placeholder': 'employ_to', 'class': 'form-control', 'type': 'date'}),
#             'content': forms.TextInput(attrs={'placeholder': 'content', 'class': 'form-control'}),
#         }


