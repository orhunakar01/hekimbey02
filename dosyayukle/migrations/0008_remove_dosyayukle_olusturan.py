# Generated by Django 2.2 on 2020-10-28 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dosyayukle', '0007_dosyayukle_olusturan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosyayukle',
            name='Olusturan',
        ),
    ]