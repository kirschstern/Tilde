# Generated by Django 2.1.5 on 2020-06-03 07:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum_tracking', '0003_auto_20200603_0451'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkshpAttendance',
            new_name='WorkshopAttendance',
        ),
    ]
