# Generated by Django 4.1.7 on 2023-02-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagasemprego',
            name='professor',
        ),
    ]