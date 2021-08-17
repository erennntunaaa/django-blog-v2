# Generated by Django 3.2.5 on 2021-08-14 20:28

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='Enter your bio details here.', max_length=400)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', 'bio'],
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=100)),
                ('about_subtitle', models.CharField(max_length=250)),
                ('about_header_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('about_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('contact_title', models.CharField(max_length=100)),
                ('contact_subtitle', models.CharField(max_length=250)),
                ('contact_header_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('contact_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('index_title', models.CharField(max_length=100)),
                ('index_subtitle', models.CharField(max_length=250)),
                ('index_header_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('index_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('login_background', models.ImageField(blank=True, null=True, upload_to='')),
                ('register_background', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('subtitle', models.CharField(max_length=200)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogauthor')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]