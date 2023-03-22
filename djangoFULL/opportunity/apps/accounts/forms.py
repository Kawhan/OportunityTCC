from accounts.models import User
from accounts.validator import *
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.safestring import mark_safe
from tempus_dominus.widgets import DatePicker

from .models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Coloque seu e-mail dcx'
        self.fields['password'].widget.attrs['placeholder'] = 'Coloque sua senha'

    class Meta:
        model = User
        fields = ['username', 'password', 'captcha']


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    error_css_class = 'error'
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Coloque seu e-mail dcx'
        self.fields['username'].widget.attrs['placeholder'] = 'Coloque seu username login'
        self.fields['password1'].widget.attrs['placeholder'] = 'Coloque sua senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Coloque sua senha'

    class Meta:
        model = User
        fields = ['username',
                  'email', 'password1', 'password2', 'captcha']
        # help_texts = {
        #     'username': mark_safe(
        #         '<div class="teste">\
        #             <ul>\
        #                 <li>Username deve ser único e não pode conter números</li>\
        #                 <li>Por favor, evitar espeços entre o username</li>\
        #             <ul/>\
        #         </div>'
        #     ),
        #     'email': mark_safe(
        #         '<div>\
        #             <ul>\
        #                 <li>Digite um e-mail valido</li>\
        #                 <li>Digite um e-mail do dominio DCX</li>\
        #             <ul/>\
        #         </div>'
        #     ),
        # }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

    def is_valid(self):
        result = super().is_valid()
        # loop on *all* fields if key '__all__' found else only on errors:
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})

        return result

    # def clean(self):
    #     email = self.cleaned_data.get("email")
    #     lista_de_erros = {}

    #     email_not_dcx(email, "email", lista_de_erros)

    #     if lista_de_erros is not None:
    #         for erro in lista_de_erros:
    #             mensagem_error = lista_de_erros[erro]
    #             self.add_error(erro, mensagem_error)

    #     return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    error_css_class = 'my_error_class'

    class Meta:
        model = UserProfile
        fields = '__all__'
        labels = {'nome': 'Nome <span class="teste">*</span>', 'idade': 'Idade <span class="teste">*</span>',
                  'matricula': 'Matricula <span class="teste">*</span>', 'periodo_ingresso': 'Periodo de Ingresso <span class="teste">*</span>', 'curso': 'Seu curso <span class="teste">*</span>'}
        widgets = {
            'user': forms.HiddenInput,
            'is_verify': forms.HiddenInput,
            # 'nota_estrutura'
        }
        # help_texts = {
        #     'nome': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque seu nome completo</li>\
        #         <ul/>'
        #     ),
        #     'periodo': mark_safe(
        #         '<ul class="listError">\
        #             <li>O período  deve ser válido dentro do limite</li>\
        #             <li>Evitar colocar período  falsos</li>\
        #         <ul/>'
        #     ),
        #     'matricula': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque sua matricula verdadeira</li>\
        #         <ul/>'
        #     ),
        #     'cra':  mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque valores possitivos e dentro do escopo de 0 a 10</li>\
        #         <ul/>'
        #     ),
        #     'idade': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque valores possitivos</li>\
        #         <ul/>'
        #     ),
        #     'curso': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque seu curso verdadeiro</li>\
        #             <li>Curso não pode ser vazio</li>\
        #         <ul/>'
        #     ),
        #     'nota_introducao': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque sua nota na cadeira de Introdução a Programação</li>\
        #             <li>Este campo não pode ser vázio</li>\
        #             <li>Colocar uma nota entre 0 e 10</li>\
        #         <ul/>'
        #     ),
        #     'nota_POO': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque sua nota na cadeira de Programação orientada a objetos</li>\
        #             <li>Caso não tenha cursado pode deixar vazio</li>\
        #             <li>Colocar uma nota entre 0 e 10</li>\
        #         <ul/>'
        #     ),
        #     'nota_linguagem':  mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque sua nota na cadeira de Linguagem de programação</li>\
        #             <li>Caso não tenha cursado pode deixar vazio</li>\
        #             <li>Colocar uma nota entre 0 e 10</li>\
        #         <ul/>'
        #     ),
        #     'nota_estrutura': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque sua nota na cadeira de Estrutua de dados</li>\
        #             <li>Caso não tenha cursado pode deixar vazio</li>\
        #             <li>Colocar uma nota entre 0 e 10</li>\
        #         <ul/>'
        #     ),
        #     'disposicao': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque sim caso tenha 20 horas semanais disponiveis exclusivamente para o projeto</li>\
        #             <li>Este campo não pode ficar vazio</li>\
        #         <ul/>'
        #     ),
        #     'numero_disciplinas': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque o número de disciplinas que está cursando esse semestre</li>\
        #             <li>Este campo só aceita valores possítivos</li>\
        #             <li>Este campo não pode ficar vazio</li>\
        #         <ul/>'
        #     ),
        #     'link_git_hub': mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque o link do seu GITHUB</li>\
        #             <li>Este campo pode ficar vazio</li>\
        #         <ul/>'
        #     ),
        #     'link_linkedin':  mark_safe(
        #         '<ul class="listError">\
        #             <li>Coloque o link do seu Linkedin</li>\
        #             <li>Este campo pode ficar vazio</li>\
        #         <ul/>'
        #     ),
        # }

    def clean(self):
        user = self.cleaned_data.get('user')
        nome = self.cleaned_data.get("nome")
        idade = self.cleaned_data.get("idade")
        matricula = self.cleaned_data.get("matricula")
        periodo_ingresso = self.cleaned_data.get("periodo_ingresso")
        curso = self.cleaned_data.get("curso")

        lista_de_erros = {}

        nome_invalid(nome, user, 'nome', lista_de_erros)
        idade_invalid(idade, 'idade', lista_de_erros)
        matricula_invalid(matricula, user, 'matricula', lista_de_erros)
        curso_invalid(curso, 'curso', lista_de_erros)

        # print(lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_error = lista_de_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data

    def is_valid(self):
        result = super().is_valid()
        # loop on *all* fields if key '__all__' found else only on errors:
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})

        return result


class UserProfileFormAdmin(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        labels = {'nome': 'Nome', 'idade': 'Idade',
                  'matricula': 'Matricula', 'curso': 'Seu curso', 'periodo_ingresso': 'Periodo de ingresso'}
        widgets = {
            'user': forms.HiddenInput,
            # 'data_ingresso': DateInput(),
            # 'data_estimada_saida': DateInput()
        }
        help_texts = {
            'nome': mark_safe(
                '<ul class="listError">\
                    <li>Coloque seu nome completo</li>\
                <ul/>'
            ),
            'matricula': mark_safe(
                '<ul class="listError">\
                    <li>Coloque sua matricula verdadeira</li>\
                <ul/>'
            ),
            'idade': mark_safe(
                '<ul class="listError">\
                    <li>Coloque valores possitivos</li>\
                <ul/>'
            ),
            'curso': mark_safe(
                '<ul class="listError">\
                    <li>Coloque seu curso verdadeiro</li>\
                    <li>Curso não pode ser vazio</li>\
                <ul/>'
            ),
            'periodo_ingresso': mark_safe(
                '<ul class="listError">\
                    <li>Coloque seu periodo de ingresso verdadeiro</li>\
                    <li>Periodo de ingresso não pode ser vazio</li>\
                <ul/>'
            ),
        }

    def clean(self):
        user = self.cleaned_data.get('user')
        nome = self.cleaned_data.get("nome")
        idade = self.cleaned_data.get("idade")
        matricula = self.cleaned_data.get("matricula")
        periodo_ingresso = self.cleaned_data.get("periodo_ingresso")
        curso = self.cleaned_data.get("curso")

        lista_de_erros = {}

        nome_invalid(nome, user, 'nome', lista_de_erros)
        idade_invalid(idade, 'idade', lista_de_erros)
        matricula_invalid(matricula, user, 'matricula', lista_de_erros)
        curso_invalid(curso, 'curso', lista_de_erros)

        # print(lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_error = lista_de_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data
