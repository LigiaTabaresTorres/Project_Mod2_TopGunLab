# Generated by Django 4.1.10 on 2023-07-12 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Evaluation",
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
                ("name", models.CharField(blank=True, max_length=100, unique=True)),
                ("symbol", models.CharField(max_length=10, unique=True)),
                ("create_time", models.DateTimeField()),
                ("update_time", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="FinancialData",
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
                ("year", models.IntegerField()),
                ("activos_corrientes", models.FloatField(default=0.0)),
                ("pasivos_corrientes", models.FloatField(default=0.0)),
                ("inventario", models.FloatField(default=0.0)),
                ("efectivo", models.FloatField(default=0.0)),
                ("deuda_pasivos", models.FloatField(default=0.0)),
                ("patrimonio", models.FloatField(default=0.0)),
                ("rotacion_inventario", models.FloatField(default=0.0)),
                ("ventas", models.FloatField(default=0.0)),
                ("activo_fijo", models.FloatField(default=0.0)),
                ("beneficio_neto", models.FloatField(default=0.0)),
                ("dividendos", models.FloatField(default=0.0)),
                ("acciones_totales", models.FloatField(default=0.0)),
                ("precio_acción", models.FloatField(default=0.0)),
                ("acciones_propias", models.FloatField(default=0.0)),
                ("create_time", models.DateTimeField()),
                ("update_time", models.DateTimeField()),
                (
                    "evaluation_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Analysis.evaluation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Indicator",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("type_index", models.CharField(max_length=100, null=True)),
                ("formula", models.CharField(max_length=100)),
                ("create_time", models.DateTimeField()),
                ("update_time", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                (
                    "user_name",
                    models.CharField(blank=True, max_length=100, unique=True),
                ),
                ("password", models.CharField(blank=True, max_length=100, unique=True)),
                ("email", models.CharField(blank=True, max_length=100, unique=True)),
                ("create_time", models.DateTimeField()),
                ("update_time", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="IndicatorValue",
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
                ("value", models.FloatField(default=0.0)),
                ("create_time", models.DateTimeField()),
                ("update_time", models.DateTimeField()),
                (
                    "FinancialData_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Analysis.financialdata",
                    ),
                ),
                ("Indicator_id", models.ManyToManyField(to="Analysis.indicator")),
            ],
        ),
    ]
