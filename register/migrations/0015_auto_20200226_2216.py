# Generated by Django 3.0.3 on 2020-02-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_list_emp_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_emp',
            name='Position',
            field=models.CharField(default='หผ.', max_length=20, null=True),
        ),
    ]
