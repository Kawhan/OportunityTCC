# Generated by Django 4.1.7 on 2023-02-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagasemprego',
            name='dataCadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]