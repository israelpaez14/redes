# Generated by Django 2.1.1 on 2019-05-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedesProyecto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='hora',
        ),
        migrations.AddField(
            model_name='horario',
            name='hora_final',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='hora_inicio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
