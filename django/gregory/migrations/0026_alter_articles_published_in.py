# Generated by Django 4.0.4 on 2022-09-26 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregory', '0025_articles_published_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='published_in',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
