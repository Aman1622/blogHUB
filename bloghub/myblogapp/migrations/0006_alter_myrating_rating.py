# Generated by Django 5.0.2 on 2024-02-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0005_rename_rating_myrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrating',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
