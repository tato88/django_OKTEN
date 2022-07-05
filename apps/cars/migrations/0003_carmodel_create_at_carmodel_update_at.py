# Generated by Django 4.0.5 on 2022-06-29 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carmodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]