# Generated by Django 4.0.6 on 2022-07-19 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_branch_contractor_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonItemBarcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.commonitem')),
            ],
        ),
    ]