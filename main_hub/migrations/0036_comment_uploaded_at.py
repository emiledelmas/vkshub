# Generated by Django 2.2.5 on 2019-11-23 11:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0035_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
