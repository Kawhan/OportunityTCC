from datetime import datetime

from django import forms
from project.models import vagasEmprego
from tempus_dominus.widgets import DatePicker


class JobForm(forms.ModelForm):
    class Meta:
        model = vagasEmprego
        fields = '__all__'
        widgets = {
            'dataFechamento': DatePicker(),
            'professor': forms.HiddenInput,
        }
