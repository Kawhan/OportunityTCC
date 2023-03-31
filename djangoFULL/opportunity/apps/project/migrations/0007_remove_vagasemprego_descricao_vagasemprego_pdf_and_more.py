# Generated by Django 4.1.7 on 2023-03-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_vagasemprego_tipo_vaga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagasemprego',
            name='descricao',
        ),
        migrations.AddField(
            model_name='vagasemprego',
            name='pdf',
            field=models.FileField(default='', upload_to='fotos/%d/%m/%Y/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vagasemprego',
            name='tipo_vaga',
            field=models.CharField(choices=[('PE', 'Projeto de extensão'), ('ES', 'Estágio'), ('PP', 'Projeto de Pesquisa')], max_length=2),
        ),
    ]
