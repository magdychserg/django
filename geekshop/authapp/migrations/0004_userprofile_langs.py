# Generated by Django 3.2 on 2021-12-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='langs',
            field=models.CharField(blank=True, default='EN', max_length=128, verbose_name='Язык'),
        ),
    ]
