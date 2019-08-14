# Generated by Django 2.2.3 on 2019-08-14 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('stack_it', '0004_auto_20190813_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='main_site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages_as_main_site', to='sites.Site', verbose_name='Main Site'),
        ),
    ]
