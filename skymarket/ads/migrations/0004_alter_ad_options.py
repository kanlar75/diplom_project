# Generated by Django 3.2.6 on 2023-12-09 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_comment_ad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['-created_at'], 'verbose_name': 'объявление', 'verbose_name_plural': 'объявления'},
        ),
    ]
