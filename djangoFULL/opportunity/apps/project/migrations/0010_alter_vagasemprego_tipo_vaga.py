# Generated by Django 4.1.7 on 2023-04-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_remove_vagasemprego_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagasemprego',
            name='tipo_vaga',
            field=models.CharField(choices=[('PE', 'Projeto de extensão'), ('PP', 'Projeto de Pesquisa'), ('ES', 'Estágio')], max_length=2),
        ),
    ]
