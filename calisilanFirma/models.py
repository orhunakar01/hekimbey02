from datetime import date
from django.db import models
from isyeriekle.models import isyeri


class calisilanFirmalar(models.Model):

    ekle1=(
        ('Az Tehlikeli','Az Tehlikeli') ,
        ('Tehlikeli','Tehlikeli') ,
        ('Çok Tehlikeli' , 'Çok Tehlikeli') ,
        )

    Sirket = models.ForeignKey(isyeri, on_delete=models.CASCADE,blank=True,null=True)
    firmaAd=models.CharField(max_length=200,verbose_name='Çalışılacak Firma Adı')
    SicilNumarasi=models.CharField(max_length=110,verbose_name="Çalışılacak Firma'nın Sicil No")
    tehlikeSinif=models.CharField(choices=ekle1, max_length=60, verbose_name='Tehlike Sınıfı')
    isyeriCalisanSayisi=models.PositiveIntegerField(verbose_name='Çalışan sayısı')
    isyeriBolge=models.CharField(max_length=40,verbose_name='Bölge')
    isyeri_ilcesi=models.CharField(max_length=50,verbose_name='İlçe')
    ad_soyad=models.CharField(max_length=100 , verbose_name='Yetkili Ad Soyad')
    telefon=models.CharField(max_length=100,verbose_name='Yetkili Telefonu')
    e_posta=models.CharField(max_length=200,verbose_name='Yetkili E - Posta')
    kayitTarih=models.DateField(default=date.today)

    def publish(self):
        self.kayitTarih = date.today()
        self.save()


    def __str__(self):
        return "{} - {}".format(self.firmaAd, self.SicilNumarasi)


