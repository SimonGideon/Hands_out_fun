# Generated by Django 3.2.4 on 2021-07-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0008_auto_20210726_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]