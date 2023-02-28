from datetime import datetime

from django import forms
from django.conf import settings
from project.models import vagasEmprego
from tempus_dominus.widgets import DatePicker


class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(forms.ModelForm):

    class Meta:
        model = vagasEmprego
        fields = '__all__'
        widgets = {
            'dataFechamento': DateInput(attrs={'placeholder': '%d/%m/%Y'}),
            'dataCadastro':  DateInput(),
            'aluno': forms.MultipleHiddenInput,
            'professor': forms.HiddenInput
        }
