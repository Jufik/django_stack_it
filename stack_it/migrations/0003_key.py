# Generated by Django 2.2.3 on 2019-07-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack_it', '0002_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='key',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Key for development'),
        ),

    ]
