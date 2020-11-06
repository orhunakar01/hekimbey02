from django import forms
from .models import EvrakAdi
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class EvrakAdiForm(forms.ModelForm):

    class Meta:
        model=EvrakAdi
        fields=[
            'sira_no',
            'evrak_adi',
            'az_tehlike',
            'tehlike',
            'cok_tehlike',

        ]