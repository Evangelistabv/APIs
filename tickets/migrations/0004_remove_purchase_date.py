# Generated by Django 4.2.11 on 2024-06-14 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0003_rename_customer_purchase_id_ticket"),
    ]

    operations = [
        migrations.RemoveField(model_name="purchase", name="date",),
    ]
