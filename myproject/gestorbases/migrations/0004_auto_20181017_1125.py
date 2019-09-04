# Generated by Django 2.1.1 on 2018-10-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorbases', '0003_auto_20181008_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atualizacao',
            name='origem_dados',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='base',
            name='descricao',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='base',
            name='host',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='base',
            name='owner',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tabela',
            name='esquema',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tabela',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
