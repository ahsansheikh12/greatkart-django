from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class' : 'form-control',
    }))
    repeat_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password Again',
        'class': 'form-control',
    }))
    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] ='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] ='Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] ='Enter email'
        self.fields['phone_number'].widget.attrs['placeholder'] ='Enter Phone'

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data=super(RegistrationForm, self).clean()
        password=cleaned_data.get('password')
        repeat_password=cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise forms.ValidationError(
                "password does not match !"
            )        