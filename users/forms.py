from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('user', "Простой пользователь"),
        ('company', "Компания")
    )
    username = forms.CharField(
        label="Укажите ваш логин", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Логин'
            }
        )
    )
    email = forms.CharField(
        label="Укажите ваш email", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Email',
                'type': 'email'
            }
        )
    )
    first_name = forms.CharField(
        label="Укажите ваше имя", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Имя'
            }
        )
    )
    last_name = forms.CharField(
        label="Укажите вашу фамилию", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Фамилия'
            }
        )
    )
    password1 = forms.CharField(
        label="Укажите пароль", 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Пароль'
            }
        )
    )
    password2 = forms.CharField(
        label="Повторите пароль", 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Повторите пароль'
            }
        )
    )
    role = forms.ChoiceField(
        choices = ROLE_CHOICES, 
        label="Выберите вашу роль", 
        initial='', 
        widget=forms.RadioSelect(
            attrs={'class':'radio'}
        ), 
        required=True
    )
    phone = forms.CharField(
        label="Телефон", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Телефонный номер'
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'email',  'phone', 'first_name', 'last_name', 'password1', 'password2', 'role')