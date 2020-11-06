from django import forms
from django.contrib.auth.models import User
from django.forms import Select
from django.contrib.auth import authenticate

from evrakAdi.models import EvrakAdi
from isyeriekle.models import isyeri
from calisilanFirma.models import calisilanFirmalar
from calisilanFirma.forms import calisilanFirmalarForm
from eslestirme.models import Eslestirme
from collections import UserList
from bootstrap_datepicker_plus import DatePickerInput , TimePickerInput , DateTimePickerInput , MonthPickerInput , \
    YearPickerInput
from .models import DosyaYukle


class DosyaYukleForm2(forms.ModelForm):
    isyeri = forms.ModelChoiceField(
        queryset=isyeri.objects.order_by('isyeriAdi') ,
        widget=Select(attrs={'class': 'isyeri'}) , label='Şirket Adı ' ,
        required=True
    )


    projeAdi = forms.ModelChoiceField(
        queryset=calisilanFirmalar.objects.order_by('firmaAd') ,
        widget=Select(attrs={'class': 'projeAdi'}) ,
        label='Proje Adı' ,
        required=True
    )

    evrakAdi = forms.ModelChoiceField(
        queryset=EvrakAdi.objects.order_by('evrak_adi') ,
        widget=Select(attrs={'class': 'evrakAdi'}) ,
        label='Evrak Adı' ,
        required=True
    )

    class Meta:
        model = DosyaYukle
        fields = [
            'Olusturan' ,
            'isyeri' ,
            'projeAdi' ,
            'evrakAdi' ,
            'dosyaYuklenmeTarihi' ,
            'GecerlilikTarihi',
            'Dosya' ,
            'onay' ,
            'red' ,
            'Aciklama' ,
            'tarih',


        ]
        widgets = {
            'dosyaYuklenmeTarihi': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr" ,
            }) ,

            'tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr" ,

            }) ,
            'GecerlilikTarihi': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr" ,

            }) ,
            'Aciklama': forms.Textarea(attrs={'rows': 3 , 'cols': 10}) ,
        }


class DosyaYukle2Form(forms.ModelForm):
    model = DosyaYukle
    fields = [
        'Olusturan' ,
        'isyeri' ,
        'projeAdi' ,
        'evrakAdi' ,
        'dosyaYuklenmeTarihi' ,
        'GecerlilikTarihi' ,
        'Dosya' ,
        'onay' ,
        'red' ,
        'Aciklama' ,
        'tarih' ,

    ]
    widgets = {
        'dosyaYuklenmeTarihi': DatePickerInput(format='%d/%m/%Y' , options={
            "format": "DD/MM/YYYY" ,  # moment date-time format
            "showClose": True ,
            "showClear": True ,
            "showTodayButton": True ,
            "locale": "tr"
        }) ,
        'tarih': DatePickerInput(format='%d/%m/%Y' , options={
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

        'Aciklama': forms.Textarea(attrs={'rows': 3 , 'cols': 10}) ,

    }