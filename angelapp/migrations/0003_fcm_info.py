# Generated by Django 2.1.2 on 2018-11-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angelapp', '0002_auto_20181122_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='fcm_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm_token', models.CharField(max_length=400)),
            ],
        ),
    ]
