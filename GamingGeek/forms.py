from django import forms

class loginForm(forms.Form):

    username = forms.CharField(label='uname', max_length=100)
    password = forms.CharField(label='psw', max_length=100)
