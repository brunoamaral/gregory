# Generated by Django 4.0.4 on 2022-10-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregory', '0029_alter_articles_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='access',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('open', 'Open'), ('restricted', 'Restricted')], default=None, max_length=50, null=True),
        ),
    ]
