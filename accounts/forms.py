from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
class RegistrationForm(UserCreationForm):
    captcha = CaptchaField()
    email = forms.EmailField(max_length=256, help_text="Required Email", required=True )
    class Meta:
        model = User
        fields = ('username','email','password1','password2', 'captcha')
class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
    username = forms.CharField(max_length=256, required=True)
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput)
    def confirm_login_allowed(self , user):
        pass