# Generated by Django 5.0.6 on 2024-06-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuz', '0003_university_slug_alter_feedback_university_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
