# Generated by Django 4.1.2 on 2022-11-12 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_published',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='short_content',
            new_name='resumen',
        ),
    ]
