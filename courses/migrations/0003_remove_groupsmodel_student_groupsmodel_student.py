# Generated by Django 4.1.7 on 2023-02-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupsmodel',
            name='student',
        ),
        migrations.AddField(
            model_name='groupsmodel',
            name='student',
            field=models.ManyToManyField(related_name='group', to='users.studentsmodel'),
        ),
    ]
