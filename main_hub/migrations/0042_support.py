# Generated by Django 2.2.5 on 2020-02-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0041_translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
