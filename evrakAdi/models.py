from django.db import models
from datetime import date

class EvrakAdi(models.Model):
    sira_no=models.PositiveIntegerField(verbose_name='Sıra No',blank=False,null=False)
    evrak_adi=models.CharField(max_length=300,verbose_name='Evrak Adı',blank=False,null=False)
    az_tehlike=models.PositiveIntegerField(verbose_name='Az Tehlikeli için Süre(Ay)')
    tehlike=models.PositiveIntegerField(verbose_name='Tehlikeli için Süre(Ay)')
    cok_tehlike=models.PositiveIntegerField(verbose_name='Çok Tehlikeli için Süre(Ay)')

    def __str__(self):
        return self.evrak_adi

