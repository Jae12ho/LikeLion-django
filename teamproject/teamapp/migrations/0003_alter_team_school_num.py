# Generated by Django 3.2.2 on 2021-05-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0002_alter_team_school_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='school_num',
            field=models.CharField(max_length=200),
        ),
    ]