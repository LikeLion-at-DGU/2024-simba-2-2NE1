# Generated by Django 5.0.6 on 2024-06-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_varsity_like_count_varsitylike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varsitylike',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to='main.varsity'),
        ),
    ]
