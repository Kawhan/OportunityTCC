# Generated by Django 4.1.5 on 2023-01-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_django', '0002_alter_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verify_staff_user',
            field=models.BooleanField(default=False),
        ),
    ]
