from django import forms
from django.forms import Select
from isyeriekle.models import isyeri
from .models import calisilanFirmalar
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class calisilanFirmalarForm(forms.ModelForm):
    Sirket=forms.ModelChoiceField(
        queryset=isyeri.objects.all().order_by('isyeriAdi') ,
        widget=Select(attrs={'class':'Sirket'}) ,

    )
    class Meta:
        model=calisilanFirmalar
        fields = [
            'Sirket',
            'firmaAd',
            'SicilNumarasi',
            'tehlikeSinif',
            'isyeriCalisanSayisi',
            'isyeriBolge',
            'isyeri_ilcesi',
            'ad_soyad',
            'telefon',
            'e_posta',
            'kayitTarih',

        ]
        widgets = {
            'kayitTarih': DatePickerInput(format='%d/%m/%Y',options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "locale":"tr"
                }),
        }
