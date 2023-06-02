from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from codemirror import CodeMirrorTextarea

class edit_new_code(forms.Form):

    code_title = forms.CharField(label = 'title',required=True)
    code_description = forms.CharField(help_text="Write a small description to explain the goal of your code, on which board it will be upload and how it can be upgraded",required=True)
    code_content = forms.CharField(help_text='write your code here',required=True)
    code_language = forms.CharField(required=True)
    def clean_code_content(self):
        data = self.cleaned_data['code_content']
        if len(data)==0: 
            raise ValidationError(_('Invalid Content - empty'))
        return data
    def clean_code_tilte(self):
        data = self.cleaned_data['code_title']
        if len(data)==0: 
            raise ValidationError(_('Invalid Title - empty'))
        return data
    def clean_code_description(self):
        data = self.cleaned_data['code_description']
        if len(data)==0: 
            raise ValidationError(_('Invalid Description - empty'))
        return data
    def clean_code_language(self):
        data = self.cleaned_data['code_language']
        if len(data)==0: 
            raise ValidationError(_('Invalid Language - empty'))
        return data

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)