# Generated by Django 2.1.7 on 2019-04-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack_it', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='folder',
            field=models.CharField(choices=[('articles', 'articles'), ('residences', 'residences'), ('services', 'services'), ('equipe', 'equipe')], default='articles', max_length=50, verbose_name='Folder'),
        ),
    ]
