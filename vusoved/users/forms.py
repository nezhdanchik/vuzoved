from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин:",
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш логин:'})
    )
    password = forms.CharField(
        label='Пароль:',
        min_length=5,
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль:'})
    )


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={'placeholder': 'Ваш логин'}))
    password = forms.CharField(label='Пароль:',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль'}))
    password2 = forms.CharField(label='Повторите пароль:',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль ещё раз'}))
    first_name = forms.CharField(label='Имя:', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='Адрес электронной почты:',
                             widget=forms.EmailInput(attrs={'placeholder': 'Ваш email'}), required=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'password2',
            'first_name',
            'email'
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email
