# Generated by Django 3.2 on 2021-04-20 04:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido del Post'),
        ),
    ]