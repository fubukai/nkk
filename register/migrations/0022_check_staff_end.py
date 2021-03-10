# Generated by Django 3.0.3 on 2021-01-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0021_check_loginerror'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_Staff_End',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_ID', models.CharField(blank=True, max_length=10, null=True)),
                ('Status', models.CharField(blank=True, max_length=200, null=True)),
                ('Exp_Date', models.CharField(blank=True, max_length=100, null=True)),
                ('Comment', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Position', models.CharField(default='อก.', max_length=20, null=True)),
                ('Level', models.CharField(default='อก.', max_length=20, null=True)),
                ('Dept_code', models.CharField(blank=True, default='0000', max_length=20, null=True)),
                ('Dept_Short', models.CharField(blank=True, default='0000', max_length=200, null=True)),
            ],
        ),
    ]
