from datetime import date, timedelta

from django.db import models
from dosyayukle.models import DosyaYukle


class DosyaOnay(models.Model):
    isyeriAd=models.ForeignKey(DosyaYukle,on_delete=models.CASCADE,related_name='isyeriAd',blank=True,null=True)
    uzman=models.ForeignKey(DosyaYukle,on_delete=models.CASCADE,related_name='uzman',blank=True,null=True)
    projead=models.ForeignKey(DosyaYukle,on_delete=models.CASCADE,related_name='projead',blank=True,null=True)
    evrakad=models.ForeignKey(DosyaYukle,on_delete=models.CASCADE,related_name='evrakad',blank=True,null=True)
    olusturmaTarihi=models.ForeignKey(DosyaYukle,on_delete=models.CASCADE,related_name='olusturmaTarihi',blank=True,null=True)
    dosya=models.ForeignKey(DosyaYukle,on_delete=models.CASCADE,related_name='dosya',blank=True,null=True)
    aciklama=models.TextField(verbose_name='Açıklama',default='Açıklama Henüz Yok.!',blank=True,null=True,max_length=340)

    @property
    def gec(self):
        days_before = (date.today() - timedelta(days=60))
        return self.dosyayukle.GecerlilikTarihi < days_before

