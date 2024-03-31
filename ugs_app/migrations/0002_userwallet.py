# Generated by Django 5.0.3 on 2024-03-15 09:43

import datetime
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugs_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('w_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('w_balance', models.IntegerField(blank=True, null=True)),
                ('w_points', models.IntegerField(blank=True, null=True)),
                ('w_commission', models.IntegerField(blank=True, null=True)),
                ('w_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('BANNED', 'BANNED')], max_length=50)),
                ('w_dateupdate', models.TimeField(default=datetime.time(17, 43, 46, 248268))),
                ('w_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_wallet', to='ugs_app.useraccount')),
            ],
        ),
    ]
