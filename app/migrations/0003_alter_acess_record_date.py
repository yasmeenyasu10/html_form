# Generated by Django 4.2.3 on 2023-08-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_web_page_urls"),
    ]

    operations = [
        migrations.AlterField(
            model_name="acess_record", name="date", field=models.DateField(),
        ),
    ]
