# Generated by Django 4.1.7 on 2023-03-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_vagasemprego_tipo_vaga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagasemprego',
            name='tipoVaga',
        ),
        migrations.AlterField(
            model_name='vagasemprego',
            name='tipo_vaga',
            field=models.CharField(choices=[('PE', 'Projeto de extensão'), ('ES', 'Estágio'), ('PP', 'Projeto de Pesquisa')], max_length=2),
        ),
    ]