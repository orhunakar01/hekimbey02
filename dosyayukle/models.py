from datetime import date , datetime , timedelta

from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

import evrakAdi
from calisilanFirma.models import calisilanFirmalar
from eslestirme.models import Eslestirme
from evrakAdi.models import EvrakAdi
from isyeriekle.models import isyeri


class DosyaYukle(models.Model):
     isyeri=models.ForeignKey(isyeri,on_delete=models.CASCADE,verbose_name='İş Yeri Adı',related_name='isyerim',blank=True,null=True)
    # osgbUzmanAdi=models.ForeignKey(User,on_delete=models.CASCADE,related_name='osgbUzmanAdi',verbose_name='Yetkili OSGB Uzmanı',blank=True,null=True)
     projeAdi=models.ForeignKey(calisilanFirmalar,on_delete=models.CASCADE,related_name='projeAdi',verbose_name='Proje Adı',blank=True,null=True)
     evrakAdi=models.ForeignKey(EvrakAdi,on_delete=models.CASCADE,related_name='evrakAdi',verbose_name='Evrak Adı',blank=True,null=True)
     dosyaYuklenmeTarihi=models.DateField(default=date.today,verbose_name='Dosya Hazırlama Tarihi')
     Dosya=models.FileField(upload_to="documents/%Y/%m/%d",blank=False,validators=[FileExtensionValidator(allowed_extensions=['pdf' or None])],null=False,default=None)
     onay=models.BooleanField(default=False,verbose_name='Dosya Onay')
     red=models.BooleanField(default=False,verbose_name='Dosya Ret ')
     tarih=models.DateField(default=date.today,verbose_name='Dosya Onay Tarihi')
     Olusturan = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True,related_name='Olusturan',verbose_name='Oluşturan Personel')
     GecerlilikTarihi=models.DateField(default=date.today,verbose_name='Dosya Geçerlilik Tarihi',null=True,blank=True)
     Aciklama=models.TextField(blank=True,null=True)


     @property
     def gec(self):
         days_before = (date.today() - timedelta(days=60))
         return self.GecerlilikTarihi < days_before





