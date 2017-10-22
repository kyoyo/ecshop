from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import widgets
from django.contrib.auth import get_user_model
from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        # self.fields['username'].widget = widgets.TextInput(attrs={'placeholder':'username','class':'form-control'})
        # self.fields['password'].widget = widgets.PasswordInput(attrs={'placeholder':'password','class':'form-control'})

        username = forms.CharField(required=True)
        password = forms.CharField(required=True, min_length=5)

class RegisterForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder':'username','class':'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'placeholder':'email','class':'form-control'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'placeholder':'password','class':'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'placeholder':'repeat password','class':'form-control'})

    class Meta:
        model = get_user_model()
        fields = ('username','email')