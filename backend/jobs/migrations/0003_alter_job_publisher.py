# Generated by Django 3.2.16 on 2023-02-08 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('jobs', '0002_auto_20230207_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
    ]
