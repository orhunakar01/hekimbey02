# Generated by Django 2.2 on 2020-10-30 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dosyayukle', '0010_auto_20201030_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dosyayukle',
            old_name='dosyaGecerlilikTarihi',
            new_name='GecerlilikTarihi',
        ),
    ]
