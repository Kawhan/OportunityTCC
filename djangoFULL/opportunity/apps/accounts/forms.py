from accounts.validator import *
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.safestring import mark_safe
from tempus_dominus.widgets import DatePicker

from .models import User, UserProfile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text='Digite um e-mail valido e que seja do dominio DCX, por favor', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username',
                  'email', 'password1', 'password2']
        help_texts = {
            'username': mark_safe(
                '<ul>\
                    <li>Username deve ser único</li>\
                    <li>Por favor, evitar espeços entre o username</li>\
                <ul/>'
            )
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

    # def clean(self):
    #     email = self.cleaned_data.get("email")
    #     lista_de_erros = {}

    #     email_not_dcx(email, 'email', lista_de_erros)

    #     if lista_de_erros is not None:
    #         for erro in lista_de_erros:
    #             mensagem_error = lista_de_erros[erro]
    #             self.add_error(erro, mensagem_error)

    #     return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        labels = {'nome': 'Nome', 'idade': 'Idade',
                  'matricula': 'Matricula', 'data_ingresso': 'Data de Ingresso', 'data_estimada_saida': 'Data Estimada saida', 'periodo': 'Período ', 'cra': 'CRA'}
        widgets = {
            'user': forms.HiddenInput,
            # 'data_ingresso': DatePicker(),
            # 'data_saida': DatePicker()
        }
        help_texts = {
            'nome': mark_safe(
                '<ul class="listError">\
                    <li>Coloque seu nome completo</li>\
                <ul/>'
            ),
            'periodo': mark_safe(
                '<ul class="listError">\
                    <li>O período  deve ser válido dentro do limite</li>\
                    <li>Evitar colocar período  falsos</li>\
                <ul/>'
            ),
            'matricula': mark_safe(
                '<ul class="listError">\
                    <li>Coloque sua matricula verdadeira</li>\
                <ul/>'
            ),
        }

    def clean(self):
        user = self.cleaned_data.get('user')
        nome = self.cleaned_data.get("nome")
        idade = self.cleaned_data.get("idade")
        matricula = self.cleaned_data.get("matricula")
        data_ingresso = self.cleaned_data.get("data_ingresso")
        data_saida = self.cleaned_data.get("data_estimada_saida")
        periodo = self.cleaned_data.get("periodo")
        cra = self.cleaned_data.get("cra")

        lista_de_erros = {}

        nome_invalid(nome, user, 'nome', lista_de_erros)
        matricula_invalid(matricula, user, 'matricula', lista_de_erros)
        periodo_invalid(periodo, 'periodo', lista_de_erros)
        cra_invalid(cra, 'cra', lista_de_erros)
        date_in_invalid(data_ingresso, data_saida,
                        'data_ingresso', lista_de_erros)

        # print(lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_error = lista_de_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data
