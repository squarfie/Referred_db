# Generated by Django 5.2.1 on 2025-07-11 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_final_data_antibioticentry_ab_micjoined_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='final_data',
            old_name='f_Batch_Name',
            new_name='f_Batch_Code',
        ),
    ]
