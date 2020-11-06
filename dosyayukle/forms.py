from django import forms
from django.contrib.auth.models import User
from django.forms import Select
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required , permission_required
from evrakAdi.models import EvrakAdi
from isyeriekle.models import isyeri
from calisilanFirma.models import calisilanFirmalar
from calisilanFirma.forms import calisilanFirmalarForm
from eslestirme.models import Eslestirme
from collections import UserList
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from .models import DosyaYukle

class DosyaYukleForm(forms.ModelForm):

    isyeri=forms.ModelChoiceField(
        queryset=isyeri.objects.order_by('isyeriAdi') ,
        widget=Select(attrs={'class':'isyeri'}),label='Şirket Adı ',
        required=True
    )

    #
    # osgbUzmanAdi=forms.ModelChoiceField(
    #     queryset=User.objects.order_by('username') ,
    #     widget=Select(attrs={'class':'osgbUzmanAdi'}),
    #     label='Yetkili OSGB Uzmanı',
    #     required=True
    # )

    projeAdi=forms.ModelChoiceField(
        queryset=calisilanFirmalar.objects.order_by('firmaAd'),
        widget=Select(attrs={'class':'projeAdi' }),
        label='Proje Adı',
        required=True
    )

    evrakAdi=forms.ModelChoiceField(
        queryset=EvrakAdi.objects.order_by('evrak_adi'),
        widget=Select(attrs={'class': 'evrakAdi'}),
        label='Evrak Adı',
        required=True
    )

    class Meta:
        model=DosyaYukle
        fields=[
            'isyeri',
            'Olusturan',
            'projeAdi',
            'evrakAdi',
            'dosyaYuklenmeTarihi',
            'Dosya',
            'GecerlilikTarihi',

        ]
        widgets = {
            'dosyaYuklenmeTarihi': DatePickerInput(format='%d/%m/%Y',options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "locale":"tr",
                }),
            'GecerlilikTarihi': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr" ,
            }) ,

        }


class DosyaYukle2Form(forms.ModelForm):
    model = DosyaYukle
    fields = [
        'isyeri' ,
        'Olusturan' ,
        'projeAdi' ,
        'evrakAdi' ,
        'dosyaYuklenmeTarihi' ,
        'GecerlilikTarihi'
        'Dosya' ,
        'onay',
        'red',
        'Aciklama',
        'tarih',

    ]
    widgets = {
        'dosyaYuklenmeTarihi': DatePickerInput(format='%d/%m/%Y' , options={
            "format": "DD/MM/YYYY" ,  # moment date-time format
            "showClose": True ,
            "showClear": True ,
            "showTodayButton": True ,
            "locale": "tr"
        }) ,
        'GecerlilikTarihi': DatePickerInput(format='%d/%m/%Y' , options={
            "format": "DD/MM/YYYY" ,  # moment date-time format
            "showClose": True ,
            "showClear": True ,
            "showTodayButton": True ,
            "locale": "tr"
        }) ,

    }