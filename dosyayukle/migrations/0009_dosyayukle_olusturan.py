# Generated by Django 2.2 on 2020-10-28 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dosyayukle', '0008_remove_dosyayukle_olusturan'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosyayukle',
            name='Olusturan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
