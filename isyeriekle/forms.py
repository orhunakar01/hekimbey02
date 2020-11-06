from django import forms
from .models import isyeri
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class isyeriForm(forms.ModelForm):

    class Meta:
        model=isyeri
        fields = [
            'isyeriAdi',
            'isyeriBolge',
            'isyeriSicil',
            'isyeriEklenmeZamani',


        ]

        widgets = {
            'isyeriEklenmeZamani': DatePickerInput(format='%d/%m/%Y',options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "locale":"tr"
                }),
        }

