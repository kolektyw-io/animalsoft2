# Generated by Django 4.0.6 on 2022-07-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_commonitembarcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
