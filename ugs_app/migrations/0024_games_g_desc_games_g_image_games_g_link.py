# Generated by Django 5.0.3 on 2024-03-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0023_games'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='g_desc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='games',
            name='g_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='games',
            name='g_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]