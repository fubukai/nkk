# Generated by Django 3.0.3 on 2020-02-19 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20200214_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mt_user',
            name='Key_Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
