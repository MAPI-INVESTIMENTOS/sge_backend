# Generated by Django 5.0.7 on 2024-07-31 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sge_api', '0002_estudante_estudantedisciplina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudantedisciplina',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='estudantedisciplina',
            name='disciplina',
            field=models.ManyToManyField(to='sge_api.disciplina'),
        ),
    ]
