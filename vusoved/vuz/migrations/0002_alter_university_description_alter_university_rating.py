# Generated by Django 5.0.6 on 2024-06-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
