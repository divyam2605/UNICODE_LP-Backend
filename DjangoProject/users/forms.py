from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    #birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    #profile = forms.ImageField()
    #CharField, TextField, IntegerField, ForeignKey, BooleanField, DateTimeField, ImageField


    class Meta:
        model = User
        fields = ['full_name','email','password1','password2']