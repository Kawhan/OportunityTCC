# Generated by Django 4.1.7 on 2023-02-27 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProfessor', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Professor(a)',
                'verbose_name_plural': 'Professores(as)',
            },
        ),
        migrations.CreateModel(
            name='vagasEmprego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroVagas', models.IntegerField(verbose_name='Número de vagas')),
                ('nivel', models.CharField(choices=[('B', 'Basico'), ('I', 'Intermediário'), ('A', 'Avançado')], max_length=1)),
                ('horasSemana', models.IntegerField(verbose_name='Horas Semana')),
                ('valorSalario', models.FloatField(verbose_name='Valor Salario')),
                ('dataCadastro', models.DateField(default=django.utils.timezone.now, verbose_name='Data de cadastro')),
                ('tipoVaga', models.CharField(max_length=255, verbose_name='Tipo da Vaga')),
                ('beneficios', models.CharField(max_length=255, verbose_name='Beneficios')),
                ('tituloVaga', models.CharField(max_length=255, verbose_name='Titulo da Vaga')),
                ('descricao', tinymce.models.HTMLField(verbose_name='Descrição')),
                ('dataFechamento', models.DateField(verbose_name='Data de Fechamento')),
                ('disponivel', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('tipo_vaga', models.CharField(choices=[('PP', 'Projeto de Pesquisa'), ('PE', 'Projeto de extensão'), ('ES', 'Estágio')], max_length=2)),
                ('nome_empresa', models.CharField(max_length=255, verbose_name='Nome empresa ou nome projeto')),
                ('aluno', models.ManyToManyField(blank=True, to='accounts.userprofile')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.professor')),
            ],
        ),
    ]
