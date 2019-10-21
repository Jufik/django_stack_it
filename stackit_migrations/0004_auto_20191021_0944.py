# Generated by Django 2.1.5 on 2019-10-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack_it', '0003_auto_20190903_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='is_public',
        ),
        migrations.AlterField(
            model_name='page',
            name='allowed_groups',
            field=models.ManyToManyField(help_text='Which groups are allowed to see the object, page is public if left empty', to='auth.Group', verbose_name='Groups'),
        ),
    ]
