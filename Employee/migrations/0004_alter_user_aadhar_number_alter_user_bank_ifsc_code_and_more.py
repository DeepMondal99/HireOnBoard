# Generated by Django 4.0.1 on 2022-06-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_rename_bank_ifsc_code_user_bank_ifsc_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aadhar_number',
            field=models.TextField(max_length=14),
        ),
        migrations.AlterField(
            model_name='user',
            name='bank_IFSC_code',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirm_bank_IFSC_code',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='pan_number',
            field=models.CharField(max_length=10),
        ),
    ]