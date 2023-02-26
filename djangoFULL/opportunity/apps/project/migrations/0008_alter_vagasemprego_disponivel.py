# Generated by Django 4.1.7 on 2023-02-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_vagasemprego_disponivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagasemprego',
            name='disponivel',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1),
        ),
    ]
