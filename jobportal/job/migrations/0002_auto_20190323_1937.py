# Generated by Django 2.1.7 on 2019-03-23 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobuser',
            old_name='user_name',
            new_name='name',
        ),
    ]
