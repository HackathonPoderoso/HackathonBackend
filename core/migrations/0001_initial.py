# Generated by Django 4.2.6 on 2023-11-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teste",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("texto", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "verbose_name": "Teste",
                "verbose_name_plural": "Testes",
            },
        ),
    ]
