# Generated by Django 2.1.7 on 2019-03-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
