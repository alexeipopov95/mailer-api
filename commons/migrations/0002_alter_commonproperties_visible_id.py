# Generated by Django 3.2 on 2022-06-06 04:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonproperties',
            name='visible_id',
            field=models.UUIDField(default=uuid.UUID('44f518e4-7250-4940-ba8f-02bca67cdc5c')),
        ),
    ]
