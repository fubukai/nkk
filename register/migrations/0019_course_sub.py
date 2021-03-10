# Generated by Django 3.0.3 on 2020-07-23 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_list_emp_dept_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=10, null=True)),
                ('number_student', models.IntegerField(default=0, null=True)),
                ('ref_course', models.ForeignKey(default='0', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sub_Course_D', to='register.Course_D')),
            ],
        ),
    ]
