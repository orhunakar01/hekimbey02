from datetime import date

from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class egitimSlaytlari(models.Model):
    sira_no=models.PositiveIntegerField(default=0)
    ismi=models.CharField(max_length=60)
    dosya=models.FileField(upload_to="documents/sablonlar/%Y/%m/%d",blank=False,null=False)
    guncel_tarih=models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ------------------------------------------ #

class talimatlar(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ---------------------------------------  #

class sertifikalar(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

#  ------------------- 4 --------------------  #

class egitimSoru(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ------------------ 5 ------------------- #

class isizin(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ----------------- 6 -------------------- #

class zimmet(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ------------------- 7 ---------------- #

class iskaza(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ---------------- 8 --------------------- #

class corona(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi
  # -------------------  9 - -----------------#

class calisan(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ------ 10 ------ #

class destek(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ---- 11 ----- #

class egitim(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ----- 12 ------ #

class calisma(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

# ------- 13 ------- #,
class degerlendirme(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

class onayli(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

class isteslim(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi


class saha(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

class kurul(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

class yonerge(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

class ekip(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi

class saglik(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi


class acil(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi


class diger(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi


class diger2(models.Model):
    sira_no = models.PositiveIntegerField(default=0)
    ismi = models.CharField(max_length=60)
    dosya = models.FileField(upload_to="documents/sablonlar/%Y/%m/%d" , blank=False , null=False)
    guncel_tarih = models.DateField(default=date.today)

    def __str__(self):
        return self.ismi