# Generated by Django 4.0.1 on 2022-06-27 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_alter_user_physically_handicapped'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bank_ifsc_code',
            new_name='bank_IFSC_code',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='confirm_bank_ifsc_code',
            new_name='confirm_bank_IFSC_code',
        ),
    ]
