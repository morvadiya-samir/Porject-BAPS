# Generated by Django 4.2.8 on 2024-08-02 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mandir", "0001_initial"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="khsetra",
            name="mandir",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mandir.mandir",
            ),
        ),
        migrations.DeleteModel(
            name="Mandir",
        ),
    ]
