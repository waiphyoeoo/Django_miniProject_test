from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, models
from seprateApp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        #or
        #fields = ['status','customer']

class CustomerProfile(ModelForm):
    class Meta:
        model = Customer
        fields = ['email','phonenumber','profile_pic']

       # exclude = ['user']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
