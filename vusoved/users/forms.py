from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label="Имя:",
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя:'})
    )
    password = forms.CharField(
        label='Пароль:',
        min_length=5,
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Ваше имя:'})
    )