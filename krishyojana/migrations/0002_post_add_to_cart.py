# Generated by Django 3.1.1 on 2020-09-25 08:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('krishyojana', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='add_to_cart',
            field=models.ManyToManyField(blank=True, default=None, related_name='add_to_cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
