# Generated by Django 3.1.3 on 2020-11-10 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('admin_users', models.ManyToManyField(blank=True, related_name='admin_morty_projects', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='morty_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
