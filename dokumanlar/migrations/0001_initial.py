# Generated by Django 2.2 on 2020-10-31 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='egitimSlaytlari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sira_no', models.PositiveIntegerField(default=0)),
                ('ismi', models.CharField(max_length=60)),
                ('dosya', models.FileField(upload_to='documents/sablonlar/%Y/%m/%d')),
                ('guncel_tarih', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
