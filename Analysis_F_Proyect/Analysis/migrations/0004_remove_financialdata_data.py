# Generated by Django 4.2.3 on 2023-07-09 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Analysis", "0003_evaluation_name_alter_financialdata_evaluation_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="financialdata",
            name="data",
        ),
    ]