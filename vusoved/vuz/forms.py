from django import forms


class NameForm(forms.Form):
    your_name = forms.EmailField(label="Your name", max_length=100)


class FeedbackForm(forms.Form):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Ваш отзыв'}), max_length=1000)
    rate = forms.IntegerField(label="Ваша оценка", widget=forms.Select(choices={i:i for i in range(1, 11)}))