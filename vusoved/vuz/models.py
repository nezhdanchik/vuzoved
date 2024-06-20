from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    rating = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('university', kwargs={'slug_university': self.slug})

class Feedback(models.Model):
    body = models.TextField(verbose_name='Текст отзыва')
    rate_choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))
    rate = models.IntegerField(choices=rate_choices, verbose_name='Оценка')
    time_created = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='feedbacks')

    def __str__(self):
        return f'{self.body[:25]}... by {self.user}'


class User(models.Model):
    name = models.CharField(max_length=255)
    role_choices = {
        'student': 'Студент',
        'moderator': 'Модератор',
        'applicant': 'Абитуриент',
    }
    role = models.CharField(max_length=255, choices=role_choices)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


from transliterate import translit


def convert_russian_to_slug(s: str):
    return slugify(translit(s, reversed=True))
