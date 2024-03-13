# Generated by Django 5.0.2 on 2024-03-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Endereco",
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
                ("rua", models.CharField()),
                ("numero", models.CharField()),
                ("cep", models.IntegerField()),
                ("cidade", models.CharField()),
                ("estado", models.CharField(max_length=2)),
            ],
        ),
    ]