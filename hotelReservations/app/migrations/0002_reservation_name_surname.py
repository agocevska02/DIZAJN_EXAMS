# Generated by Django 5.0.6 on 2024-06-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='name_surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
