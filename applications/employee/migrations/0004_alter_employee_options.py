# Generated by Django 4.1.7 on 2023-04-03 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['id'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
