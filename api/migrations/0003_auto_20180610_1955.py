# Generated by Django 2.0.6 on 2018-06-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180610_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='derrotas',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='gols_marcados',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='gols_sofridos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='vitorias',
            field=models.IntegerField(null=True),
        ),
    ]