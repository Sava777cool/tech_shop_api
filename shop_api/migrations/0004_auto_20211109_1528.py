# Generated by Django 3.2.9 on 2021-11-09 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0003_auto_20211109_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status_ready',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='score',
            name='status_paid',
        ),
    ]
