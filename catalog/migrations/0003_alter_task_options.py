# Generated by Django 5.1.1 on 2024-09-08 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['datetime', '-is_done']},
        ),
    ]
