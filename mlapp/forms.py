from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class DrugPredictionForm(forms.Form):
    AGE_CHOICES = [(i, i) for i in range(10, 101)]
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    BP_CHOICES = [('HIGH', 'High'), ('NORMAL', 'Normal'), ('LOW', 'Low')]
    CHOLESTEROL_CHOICES = [('High', 'High'), ('Normal', 'Normal'), ('Low', 'Low')]
    
    age = forms.ChoiceField(
        choices=AGE_CHOICES, 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    sex = forms.ChoiceField(
        choices=SEX_CHOICES, 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    blood_pressure = forms.ChoiceField(
        choices=BP_CHOICES, 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-control'}), 
        label='Blood Pressure'
    )
    
    cholesterol = forms.ChoiceField(
        choices=CHOLESTEROL_CHOICES, 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    na_to_k = forms.FloatField(
        required=True, 
        min_value=0,
        max_value=50,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        label='Na to K Ratio'
    )