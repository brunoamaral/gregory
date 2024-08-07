# Generated by Django 4.0.4 on 2022-07-31 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSetting',
            fields=[
                ('setting_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=280, unique=True)),
                ('email_footer', models.TextField(blank=True, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
        ),
    ]
