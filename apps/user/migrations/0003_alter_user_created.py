# Generated by Django 4.0.4 on 2022-04-20 00:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apps_user', '0002_alter_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
