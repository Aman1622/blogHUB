# Generated by Django 5.0.2 on 2024-02-19 07:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0004_alter_rating_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='rating',
            new_name='myrating',
        ),
    ]
