# Generated by Django 4.2.11 on 2024-06-13 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_customer", models.CharField(max_length=100)),
                ("email_customer", models.EmailField(max_length=254, unique=True)),
                ("total_compra", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product", models.CharField(max_length=100)),
                ("quantity", models.PositiveIntegerField()),
                ("total_product", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchases",
                        to="tickets.customer",
                    ),
                ),
            ],
        ),
    ]
