from django import forms
from django.contrib.auth import authenticate

class formname(forms.Form):
    name    =forms.CharField(max_length=25)
    email   =forms.EmailField()
    password=forms.CharField(max_length=25,widget=forms.PasswordInput())

class login(forms.Form):
    Email=forms.EmailField()
    Password=forms.CharField(max_length=25,widget=forms.PasswordInput())

    '''def clean(self,*args,**kwargs):
        usermail=self.cleaned_data.get('Email')
        passwd=self.cleaned_data.get('Password')

        if usermail and passwd:
            user=authenticate(username=usermail,password=passwd)
            if not user:
                raise forms.ValidationError('Invalid Email')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
        return super(login,self).clean(*args,**kwargs)'''