from datetime import date

from django.db import models
from isyeriekle.models import isyeri
from calisilanFirma.models import calisilanFirmalar
from django.contrib.auth.models import User
from collections import UserList
from django.contrib.auth import authenticate
from django.utils import timezone


class Eslestirme(models.Model):
    Sirket = models.ForeignKey(isyeri, blank=True,null=True,on_delete=models.CASCADE,related_name='Sirket')
    firmaAdi=models.ForeignKey(calisilanFirmalar,blank=True,null=True,on_delete=models.CASCADE,related_name='Firma_Adi')
    firmaSicil=models.ForeignKey(calisilanFirmalar,blank=True,null=True,on_delete=models.CASCADE,related_name='firma_sicilleri_olacak')
    yetkiliOsgbUzmani_1=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='Yetki_osgb_uzm')
    yetkiliOsgbUzmani_2=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='Yetki_osgb_uzm_2')
    yetkiliOsgbUzmani_3=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='Yetki_osgb_uzm_3')
    yetkiliOsgbUzmani_4=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='Yetki_osgb_uzm_4')
    yetkiliOsgbUzmani_5=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='Yetki_osgb_uzm_5')
    yetkiliHekim=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='Yetki_hekim')
    yetkiliSaglikPersoneli=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='Yetki_sag_pers')
    atamaTarihi=models.DateField(default=date.today,verbose_name='Personeller Atanma Tarihi')



