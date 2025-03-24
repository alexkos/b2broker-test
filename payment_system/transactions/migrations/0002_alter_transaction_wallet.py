# Generated by Django 5.1.7 on 2025-03-21 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('transactions', '0001_initial'),
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='wallets.wallet'
            ),
        ),
    ]
