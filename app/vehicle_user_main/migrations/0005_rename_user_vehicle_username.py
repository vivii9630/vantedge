# Generated by Django 5.0 on 2023-12-22 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_user_main', '0004_alter_vehicle_truck_num_alter_vehicle_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='user',
            new_name='username',
        ),
    ]
