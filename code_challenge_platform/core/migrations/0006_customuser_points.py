# Generated by Django 5.1.2 on 2024-12-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_challenge_template_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
