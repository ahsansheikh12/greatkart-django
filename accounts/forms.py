from dataclasses import fields
import profile
from pyexpat import model
from django import forms
from .models import Account, UserProfile

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

class UserForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('first_name','last_name','phone_number')

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture=forms.ImageField(required=False,error_messages={'invalid':("image files only")},widget=forms.FileInput)
    class Meta:
        model=UserProfile
        fields=('address_line1','address_line2','city','state','country','profile_picture')                   

    def __init__(self,*args,**kwargs):
        super(UserProfileForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'    