from accounts.models import UserProfile
from accounts.validator import *
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from tempus_dominus.widgets import DatePicker


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text='Digite um e-mail valido, por favor', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username',
                  'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput,
            # 'data_ingresso': DatePicker(),
            # 'data_saida': DatePicker()
        }

    def clean(self):
        nome = self.cleaned_data.get("nome")
        idade = self.cleaned_data.get("idade")
        matricula = self.cleaned_data.get("matricula")
        data_ingresso = self.cleaned_data.get("data_ingresso")
        data_saida = self.cleaned_data.get("data_estimada_saida")
        periodo = self.cleaned_data.get("periodo")
        cra = self.cleaned_data.get("cra")

        lista_de_erros = {}

        nome_invalid(nome, 'nome', lista_de_erros)
        matricula_invalid(matricula, 'matricula', lista_de_erros)
        periodo_invalid(periodo, 'periodo', lista_de_erros)
        cra_invalid(cra, 'cra', lista_de_erros)
        date_in_invalid(data_ingresso, data_saida,
                        'data_ingresso', lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_error = lista_de_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data
