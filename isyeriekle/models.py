from datetime import date

from django.db import models

class isyeri(models.Model):
    isyeriAdi=models.CharField(max_length=130,verbose_name='İşyeri Adı',blank=False,null=False)
    isyeriBolge=models.CharField(max_length=30,verbose_name='İşyeri Bölgesi',blank=True,null=True)
    isyeriSicil=models.CharField(max_length=100,verbose_name='İşyeri Sicil No',blank=True,null=True)
    isyeriEklenmeZamani=models.DateField(default=date.today,)

    def publish(self):
        self.bitis = date.today()
        self.save()

    def __str__(self):
        return self.isyeriAdi
    
