from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from mandal.models import Mandal
from mandir.models import Mandir
from khsetra.models import Khsetra
from haribhakt.models import Haribhakt

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['placeholder'] = field.label

            if isinstance(field.widget, forms.CheckboxInput):
                # Add specific class for checkboxes
                field.widget.attrs['class'] = 'form-check-input my-2'

            else:
                if 'class' in field.widget.attrs:
                    field.widget.attrs['class'] += ' form-control my-2'
                else:
                    field.widget.attrs['class'] = 'form-control my-2'

class RegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control my-2'
            if field_name == 'username':
                self.fields[field_name].widget.attrs['placeholder'] = 'Username'
            elif 'password' in field_name:
                self.fields[field_name].widget.attrs['placeholder'] = 'Password'
            
            # Remove help text
            self.fields[field_name].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if field in self.errors:
                self.add_error(field, f"Please enter a valid {field.replace('_', ' ').title()}")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        if self.errors:
            self.add_error(None, "Invalid username or password")
        return cleaned_data

class MandirForm(BaseForm):
    class Meta:
        model = Mandir
        fields = '__all__'

class KhsetraForm(BaseForm):
    class Meta:
        model = Khsetra
        fields = '__all__'

# class KhsetraForm(BaseForm):
#     class Meta:
#         model = Khsetra
#         fields = [
#             'name', 'number', 'mandir', 'nirdeshak_name', 
#             'nirdeshak_contact_number', 'sanyojak_name', 
#             'sanyojak_contact_number'
#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         mandir_list = Mandir.objects.all().values_list('id', 'name')  
#         mandir_choices = [(mandir[0], mandir[1]) for mandir in mandir_list]
#         self.fields['mandir'] = forms.ChoiceField(choices=mandir_choices)
        # self.fields['mandir'].widget.attrs['class'] = ' form-select my-2'

class MandalForm(BaseForm):
    class Meta:
        model = Mandal
        fields = '__all__'

class HaribhaktForm(BaseForm):
    class Meta:
        model = Haribhakt
        fields = '__all__'
