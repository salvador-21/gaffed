# Generated by Django 5.0.3 on 2024-03-18 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0017_userwallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='user_wallet',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_wallet', to='ugs_app.userwallet'),
        ),
    ]
