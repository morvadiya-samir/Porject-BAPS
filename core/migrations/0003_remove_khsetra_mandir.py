# Generated by Django 4.2.8 on 2024-08-08 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_khsetra_mandir_delete_mandir"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="khsetra",
            name="mandir",
        ),
    ]
