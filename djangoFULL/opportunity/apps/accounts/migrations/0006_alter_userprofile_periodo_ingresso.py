# Generated by Django 4.1.7 on 2023-03-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_periodo_ingresso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='periodo_ingresso',
            field=models.CharField(blank=True, choices=[('2019.1', '2019.1'), ('2019.2', '2019.2'), ('2020.1', '2020.1'), ('2020.2', '2020.2'), ('2021.1', '2021.1'), ('2021.2', '2021.2'), ('2022.1', '2022.1'), ('2022.2', '2022.2'), ('2023.1', '2023.1'), ('2023.2', '2023.2'), ('2024.1', '2024.1'), ('2024.2', '2024.2'), ('2025.1', '2025.1'), ('2025.2', '2025.2')], max_length=6, null=True),
        ),
    ]
