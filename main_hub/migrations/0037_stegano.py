# Generated by Django 2.2.5 on 2019-12-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0036_comment_uploaded_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stegano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('picture', models.ImageField(upload_to='steganography/')),
                ('key', models.CharField(max_length=100)),
            ],
        ),
    ]
