from django import forms
from django.forms import Select
from isyeriekle.models import isyeri
from .models import egitimSlaytlari , talimatlar , sertifikalar , egitimSoru , isizin , zimmet , corona , calisan , \
    destek , egitim , calisma , degerlendirme , onayli , isteslim , saha , kurul , yonerge , ekip , saglik , acil , \
    diger , diger2
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class EgitimSlaytlariForm(forms.ModelForm):
    class Meta:
        model=egitimSlaytlari
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class talimatlarForm(forms.ModelForm):
    class Meta:
        model=talimatlar
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class sertifikalarForm(forms.ModelForm):
    class Meta:
        model=sertifikalar
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class egitimSoruForm(forms.ModelForm):
    class Meta:
        model=egitimSoru
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

# --------------------  5  -------------------- #

class isizinForm(forms.ModelForm):
    class Meta:
        model=isizin
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class zimmetForm(forms.ModelForm):
    class Meta:
        model=zimmet
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class iskazaForm(forms.ModelForm):
    class Meta:
        model=zimmet
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class coronaForm(forms.ModelForm):
    class Meta:
        model=corona
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class calisanForm(forms.ModelForm):
    class Meta:
        model=calisan
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class destekForm(forms.ModelForm):
    class Meta:
        model=destek
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class egitimForm(forms.ModelForm):
    class Meta:
        model=egitim
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class calismaForm(forms.ModelForm):
    class Meta:
        model=calisma
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class degerlendirmeForm(forms.ModelForm):
    class Meta:
        model=degerlendirme
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class onayliForm(forms.ModelForm):
    class Meta:
        model=onayli
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class isteslimForm(forms.ModelForm):
    class Meta:
        model=isteslim
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class sahaForm(forms.ModelForm):
    class Meta:
        model=saha
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class kurulForm(forms.ModelForm):
    class Meta:
        model=kurul
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class yonergeForm(forms.ModelForm):
    class Meta:
        model=yonerge
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class ekipForm(forms.ModelForm):
    class Meta:
        model=ekip
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class saglikForm(forms.ModelForm):
    class Meta:
        model=saglik
        fields = [
            'sira_no',
            'ismi',
            'dosya',
            'guncel_tarih',
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class acilForm(forms.ModelForm):
    class Meta:
        model = acil
        fields = [
            'sira_no' ,
            'ismi' ,
            'dosya' ,
            'guncel_tarih' ,
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }

class digerForm(forms.ModelForm):
    class Meta:
        model = diger
        fields = [
            'sira_no' ,
            'ismi' ,
            'dosya' ,
            'guncel_tarih' ,
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class digerForm2(forms.ModelForm):
    class Meta:
        model = diger2
        fields = [
            'sira_no' ,
            'ismi' ,
            'dosya' ,
            'guncel_tarih' ,
        ]
        widgets = {
            'guncel_tarih': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }