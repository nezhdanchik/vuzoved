from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    rating = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Feedback(models.Model):
    body = models.TextField()
    rate_choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))
    rate = models.IntegerField(choices=rate_choices)
    time_created = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='feedbacks')

    def __str__(self):
        return f'{self.body[:25]}... by {self.user}'


class User(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


from transliterate import translit


def convert_russian_to_slug(s: str):
    return slugify(translit(s, reversed=True))
