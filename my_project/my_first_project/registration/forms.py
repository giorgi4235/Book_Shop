# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Profile

#django.scsa@gmail.com


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:

        model = User
        fields = ["email","status"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            #  'last_name': forms.TextInput(attrs={'class': 'form-control'}),
         }


class UserLoginForm(forms.Form):
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm New Password')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise ValidationError('Old password is incorrect.')
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise ValidationError('The new passwords do not match.')

        return cleaned_data

    # def save(self, commit=True):
    #     new_password = self.cleaned_data.get('new_password1')
    #     self.user.set_password(new_password)
    #     if commit:
    #         self.user.save()
    #     return self.user

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['first_name','last_name']
        exclude=['uuid']
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )

#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name', 'password']
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#         }

#     def clean_confirm_password(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
#         return confirm_password


