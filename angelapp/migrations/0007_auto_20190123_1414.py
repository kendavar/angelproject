# Generated by Django 2.1.2 on 2019-01-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angelapp', '0006_angeltable_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='angeltable',
            name='created_Date',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
