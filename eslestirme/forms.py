from django import forms
from django.contrib.auth.models import User
from django.forms import Select
from django.contrib.auth import authenticate
from isyeriekle.models import isyeri
from calisilanFirma.models import calisilanFirmalar
from calisilanFirma.forms import calisilanFirmalarForm
from .models import Eslestirme
from collections import UserList
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class EslestirmeForm(forms.ModelForm):

    Sirket=forms.ModelChoiceField(
        queryset=isyeri.objects.order_by('isyeriAdi') ,
        widget=Select(attrs={'class':'Sirket'}),label='Şirket Adı ',
        required=True

    )

    firmaAdi=forms.ModelChoiceField(
        queryset=calisilanFirmalar.objects.order_by('Sirket','firmaAd') ,
        widget=Select(attrs={'class':'firmaAdi'}),label='Firma Adı ve Sicil No ',
        required=True
    )

    """firmaSicil=forms.ModelChoiceField(
        queryset=calisilanFirmalar.objects.order_by('SicilNumarasi'),
        widget=Select(attrs={'class':'firmaAdi'}),label='Firma Sicil Numara',
        required=True
    )"""

    yetkiliOsgbUzmani_1=forms.ModelChoiceField(
        queryset=User.objects.order_by('username') ,
        widget=Select(attrs={'class':'yetkiliOsgbUzmani_1'}),
        label='Yetkili OSGB Uzmanı',
        required=True
    )
    yetkiliOsgbUzmani_2=forms.ModelChoiceField(
        queryset=User.objects.order_by('username') ,
        widget=Select(attrs={'class': 'yetkiliOsgbUzmani_2'}) ,
        label='Yetkili 2. OSGB Uzmanı',
        required=False
    )
    yetkiliOsgbUzmani_3=forms.ModelChoiceField(
        queryset=User.objects.order_by('username') ,
        widget=Select(attrs={'class': 'yetkiliOsgbUzmani_3'}) ,
        label='Yetkili 3. OSGB Uzmanı',
        required=False
    )
    yetkiliOsgbUzmani_4=forms.ModelChoiceField(
        queryset=User.objects.order_by('username') ,
        widget=Select(attrs={'class': 'yetkiliOsgbUzmani_4'}) ,
        label='Yetkili 4. OSGB Uzmanı',
        required=False
    )
    yetkiliOsgbUzmani_5=forms.ModelChoiceField(
        queryset=User.objects.order_by('username') ,
        widget=Select(attrs={'class': 'yetkiliOsgbUzmani_5'}) ,
        label='Yetkili 5. OSGB Uzmanı',
        required=False
    )

    yetkiliHekim=forms.ModelChoiceField(
        queryset=User.objects.order_by('username') ,
        widget=Select(attrs={'class': 'yetkiliHekim'}) ,
        label='Yetkili Hekim ',
        required=False
    )

    yetkiliSaglikPersoneli=forms.ModelChoiceField(
        queryset=User.objects.order_by('username') ,
        widget=Select(attrs={'class': 'yetkiliSaglikPersoneli'}) ,
        label='Yetkili Sağlık Personeli ',
        required=False
    )

    class Meta:
        model=Eslestirme
        fields=[
            'Sirket',
            'firmaAdi',
            'yetkiliOsgbUzmani_1',
            'yetkiliOsgbUzmani_2',
            'yetkiliOsgbUzmani_3' ,
            'yetkiliOsgbUzmani_4' ,
            'yetkiliOsgbUzmani_5' ,
            'yetkiliHekim',
            'yetkiliSaglikPersoneli',
            'atamaTarihi',
        ]
        widgets = {
            'atamaTarihi': DatePickerInput(format='%d/%m/%Y',options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "locale":"tr"
                }),
        }
