# Generated by Django 3.2 on 2022-06-06 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailType',
            fields=[
                ('commonproperties_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commons.commonproperties')),
                ('name', models.CharField(max_length=254)),
                ('template', models.CharField(max_length=254)),
                ('is_available', models.BooleanField(default=True)),
            ],
            bases=('commons.commonproperties',),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('commonproperties_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commons.commonproperties')),
                ('title', models.CharField(max_length=254)),
                ('subject', models.CharField(max_length=254)),
                ('email_body', models.TextField()),
                ('email_from', models.EmailField(max_length=254)),
                ('email_to', models.EmailField(max_length=254)),
                ('email_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.emailtype')),
            ],
            bases=('commons.commonproperties',),
        ),
    ]
