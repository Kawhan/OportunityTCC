# Generated by Django 4.1.7 on 2023-02-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]