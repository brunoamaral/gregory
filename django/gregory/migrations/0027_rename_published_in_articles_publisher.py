# Generated by Django 4.0.4 on 2022-09-27 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gregory', '0026_alter_articles_published_in'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='published_in',
            new_name='publisher',
        ),
    ]
