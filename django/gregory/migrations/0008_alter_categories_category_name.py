# Generated by Django 4.0.3 on 2022-03-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregory', '0007_categories_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]