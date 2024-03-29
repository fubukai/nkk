# Generated by Django 3.0.3 on 2020-02-19 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20200219_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_dept',
            name='ref_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='List_Dept_Course_D', to='register.Course_D'),
        ),
        migrations.AlterField(
            model_name='list_emp',
            name='ref_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='List_Emp_Course_D', to='register.Course_D'),
        ),
    ]
