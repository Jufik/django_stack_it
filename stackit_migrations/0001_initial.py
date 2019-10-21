# Generated by Django 2.1.5 on 2019-09-03 06:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import mptt.fields
import polymorphic_tree.models
import stack_it.utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('folder', models.CharField(choices=[('folder', 'folder')], default='folder', max_length=50, verbose_name='Folder')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('alt', models.CharField(blank=True, max_length=50, verbose_name='Alternative text')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('meta_description', models.CharField(default='', help_text='keep this under 160 characters for best optimisation', max_length=250, verbose_name='Meta Description')),
                ('meta_description_en', models.CharField(default='', help_text='keep this under 160 characters for best optimisation', max_length=250, null=True, verbose_name='Meta Description')),
                ('meta_description_fr', models.CharField(default='', help_text='keep this under 160 characters for best optimisation', max_length=250, null=True, verbose_name='Meta Description')),
                ('meta_title', models.TextField(default='', help_text='keep this under 60 characters for best optimisation', verbose_name='Meta Title')),
                ('meta_title_en', models.TextField(default='', help_text='keep this under 60 characters for best optimisation', null=True, verbose_name='Meta Title')),
                ('meta_title_fr', models.TextField(default='', help_text='keep this under 60 characters for best optimisation', null=True, verbose_name='Meta Title')),
                ('tw_title', models.CharField(blank=True, help_text='Keep this under 70 characters for best optimisation', max_length=100, verbose_name='Twitter Title')),
                ('tw_title_en', models.CharField(blank=True, help_text='Keep this under 70 characters for best optimisation', max_length=100, null=True, verbose_name='Twitter Title')),
                ('tw_title_fr', models.CharField(blank=True, help_text='Keep this under 70 characters for best optimisation', max_length=100, null=True, verbose_name='Twitter Title')),
                ('tw_description', models.TextField(blank=True, help_text='Twitter description less than 200 characters', verbose_name='Twitter Description')),
                ('tw_description_en', models.TextField(blank=True, help_text='Twitter description less than 200 characters', null=True, verbose_name='Twitter Description')),
                ('tw_description_fr', models.TextField(blank=True, help_text='Twitter description less than 200 characters', null=True, verbose_name='Twitter Description')),
                ('og_title', models.CharField(blank=True, help_text='Keep it under 55 characters for best optimisation', max_length=100, verbose_name='Facebook Title')),
                ('og_title_en', models.CharField(blank=True, help_text='Keep it under 55 characters for best optimisation', max_length=100, null=True, verbose_name='Facebook Title')),
                ('og_title_fr', models.CharField(blank=True, help_text='Keep it under 55 characters for best optimisation', max_length=100, null=True, verbose_name='Facebook Title')),
                ('og_description', models.TextField(blank=True, help_text='Facebook description less than 300 characters', verbose_name='Facebook Description')),
                ('og_description_en', models.TextField(blank=True, help_text='Facebook description less than 300 characters', null=True, verbose_name='Facebook Description')),
                ('og_description_fr', models.TextField(blank=True, help_text='Facebook description less than 300 characters', null=True, verbose_name='Facebook Description')),
                ('priority', models.FloatField(default=0.5, verbose_name='Page priority for indexation')),
                ('changefreq', models.CharField(choices=[('always', 'always'), ('hourly', 'hourly'), ('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ('yearly', 'yearly'), ('never', 'never')], default='monthly', max_length=50, verbose_name='Page change frequency')),
                ('slug', models.SlugField(blank=True, max_length=500, verbose_name='Slug')),
                ('slug_en', models.SlugField(blank=True, max_length=500, null=True, verbose_name='Slug')),
                ('slug_fr', models.SlugField(blank=True, max_length=500, null=True, verbose_name='Slug')),
                ('auto_slug', models.BooleanField(default=True, help_text="When set, your slug will automatically be updated from field define in class's SLUGIFY_FROM", verbose_name='Auto Slug')),
                ('auto_slug_en', models.BooleanField(default=True, help_text="When set, your slug will automatically be updated from field define in class's SLUGIFY_FROM", verbose_name='Auto Slug')),
                ('auto_slug_fr', models.BooleanField(default=True, help_text="When set, your slug will automatically be updated from field define in class's SLUGIFY_FROM", verbose_name='Auto Slug')),
                ('ref_full_path', models.SlugField(editable=False, max_length=500, verbose_name='Denormalized full path')),
                ('ref_full_path_en', models.SlugField(editable=False, max_length=500, null=True, verbose_name='Denormalized full path')),
                ('ref_full_path_fr', models.SlugField(editable=False, max_length=500, null=True, verbose_name='Denormalized full path')),
                ('template_path', models.CharField(default='', max_length=250, verbose_name='Template Path')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=250, null=True, verbose_name='Title')),
                ('status', model_utils.fields.StatusField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=100, no_check_for_status=True)),
                ('verbose_name', models.CharField(max_length=250, verbose_name='Instance model verbose_name')),
                ('key', models.SlugField(blank=True, max_length=250, null=True, verbose_name='Key for development')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('main_site', models.ForeignKey(blank=True, help_text='In case the page is available on multiple websites, choose which one is to be considered as the main one', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages_as_main_site', to='sites.Site', verbose_name='Main Site')),
                ('meta_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meta_images', to='stack_it.Image', verbose_name='Meta Image')),
                ('og_image', models.ForeignKey(blank=True, help_text='must be at least 1200x630px', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='od_images', to='stack_it.Image', verbose_name='Facebook Image')),
                ('parent', polymorphic_tree.models.PolymorphicTreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='stack_it.Page')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_stack_it.page_set+', to='contenttypes.ContentType')),
                ('sites', models.ManyToManyField(help_text='This page will be available for each of those websites', to='sites.Site', verbose_name='Site')),
                ('tw_image', models.ForeignKey(blank=True, help_text='must be at least 120x120px', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tw_images', to='stack_it.Image', verbose_name='Twitter Image')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('key', models.CharField(max_length=50, verbose_name='Key')),
                ('content_type', models.CharField(choices=[('meta', 'Meta content'), ('value', 'Standard content')], default='value', max_length=50, verbose_name='Content Type')),
            ],
            options={
                'verbose_name': 'Page Content',
                'verbose_name_plural': 'Page Contents',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Name')),
                ('path', models.CharField(max_length=250, verbose_name='Path')),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
        ),
        migrations.CreateModel(
            name='TemplateContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('key', models.CharField(max_length=50, verbose_name='Key')),
                ('content_type', models.CharField(choices=[('meta', 'Meta content'), ('value', 'Standard content')], default='value', max_length=50, verbose_name='Content Type')),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Template',
            },
        ),
        migrations.CreateModel(
            name='ImagePageContent',
            fields=[
                ('pagecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.PageContent')),
                ('ref_image', models.ImageField(upload_to='', verbose_name='Image')),
                ('ref_alt', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alternative text')),
                ('size', models.CharField(default='800x600', max_length=50, validators=[stack_it.utils.validators.validate_image_size], verbose_name='Size')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_it.Image', verbose_name='Image instance')),
            ],
            options={
                'verbose_name': 'Image Page Content',
                'verbose_name_plural': 'Image Page Contents',
            },
            bases=('stack_it.pagecontent', models.Model),
        ),
        migrations.CreateModel(
            name='ImageTemplateContent',
            fields=[
                ('templatecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.TemplateContent')),
                ('ref_image', models.ImageField(upload_to='', verbose_name='Image')),
                ('ref_alt', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alternative text')),
                ('size', models.CharField(default='800x600', max_length=50, validators=[stack_it.utils.validators.validate_image_size], verbose_name='Size')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_it.Image', verbose_name='Image instance')),
            ],
            options={
                'verbose_name': 'Image Template Content',
                'verbose_name_plural': 'Image Template Contents',
            },
            bases=('stack_it.templatecontent', models.Model),
        ),
        migrations.CreateModel(
            name='ModelPageContent',
            fields=[
                ('pagecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.PageContent')),
                ('instance_id', models.IntegerField(null=True, verbose_name='Object id')),
                ('model_name', models.CharField(max_length=50, validators=[stack_it.utils.validators.validate_model_name], verbose_name='Model Name')),
            ],
            options={
                'verbose_name': 'Related Model Page Content',
                'verbose_name_plural': 'Related Model Page Contents',
            },
            bases=('stack_it.pagecontent', models.Model),
        ),
        migrations.CreateModel(
            name='ModelTemplateContent',
            fields=[
                ('templatecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.TemplateContent')),
                ('instance_id', models.IntegerField(null=True, verbose_name='Object id')),
                ('model_name', models.CharField(max_length=50, validators=[stack_it.utils.validators.validate_model_name], verbose_name='Model Name')),
            ],
            options={
                'verbose_name': 'Related Model Template Content',
                'verbose_name_plural': 'Related Model Template Contents',
            },
            bases=('stack_it.templatecontent', models.Model),
        ),
        migrations.CreateModel(
            name='PagePageContent',
            fields=[
                ('pagecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.PageContent')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_pagepagecontent', to='stack_it.Page', verbose_name='Page')),
            ],
            options={
                'verbose_name': 'Related Page Page Content',
                'verbose_name_plural': 'Related Page Page Contents',
            },
            bases=('stack_it.pagecontent', models.Model),
        ),
        migrations.CreateModel(
            name='PageTemplateContent',
            fields=[
                ('templatecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.TemplateContent')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_pagetemplatecontent', to='stack_it.Page', verbose_name='Page')),
            ],
            options={
                'verbose_name': 'Related Page Template Content',
                'verbose_name_plural': 'Related Page Template Contents',
            },
            bases=('stack_it.templatecontent', models.Model),
        ),
        migrations.CreateModel(
            name='TextPageContent',
            fields=[
                ('pagecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.PageContent')),
                ('value', models.TextField(verbose_name='Value')),
                ('value_en', models.TextField(null=True, verbose_name='Value')),
                ('value_fr', models.TextField(null=True, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Text Page Content',
                'verbose_name_plural': 'Text Page Contents',
            },
            bases=('stack_it.pagecontent', models.Model),
        ),
        migrations.CreateModel(
            name='TextTemplateContent',
            fields=[
                ('templatecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stack_it.TemplateContent')),
                ('value', models.TextField(verbose_name='Value')),
                ('value_en', models.TextField(null=True, verbose_name='Value')),
                ('value_fr', models.TextField(null=True, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Text Template Content',
                'verbose_name_plural': 'Text Template Contents',
            },
            bases=('stack_it.templatecontent', models.Model),
        ),
        migrations.AddField(
            model_name='templatecontent',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_stack_it.templatecontent_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='templatecontent',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='stack_it.Template', verbose_name='Template'),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='stack_it.Page', verbose_name='Page'),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_stack_it.pagecontent_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='menu',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menus', to='stack_it.Page', verbose_name='Page'),
        ),
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='stack_it.Menu'),
        ),
        migrations.AlterUniqueTogether(
            name='templatecontent',
            unique_together={('template', 'key')},
        ),
        migrations.AlterUniqueTogether(
            name='pagecontent',
            unique_together={('page', 'key')},
        ),
    ]
