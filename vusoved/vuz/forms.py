from django import forms
from .models import Feedback

class NameForm(forms.Form):
    your_name = forms.EmailField(label="Your name", max_length=100)


class FeedbackForm(forms.ModelForm):
    choices = {
        '': 'не выбрано',
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10
    }
    rate = forms.IntegerField(label="Ваша оценка", widget=forms.Select(choices=choices))
    class Meta:
        model = Feedback
        fields = ['body', 'rate']
        widgets = {
            "body": forms.Textarea(attrs={'placeholder': 'Ваш отзыв', 'maxlength': 1000,}),
        }
        labels = {
            "body": "",
        }

