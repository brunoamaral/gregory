# Generated by Django 4.0.4 on 2022-08-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregory', '0016_remove_articles_sent_to_twitter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
