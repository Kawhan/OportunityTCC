from accounts.models import User
from accounts.validator import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.safestring import mark_safe
from tempus_dominus.widgets import DatePicker

from .models import User, UserProfile


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {
            'class': 'venue-type-select', }

    class Meta:
        model = User
        fields = ['username',
                  'email', 'password1', 'password2']
        help_texts = {
            'username': mark_safe(
                '<ul  class="listError">\
                    <li>Username deve ser único e não pode conter números</li>\
                    <li>Por favor, evitar espeços entre o username</li>\
                <ul/>'
            ),
            'email': mark_safe(
                '<ul  class="listError">\
                    <li>Digite um e-mail valido</li>\
                    <li>Digite um e-mail do dominio DCX</li>\
                <ul/>'
            ),
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

    def clean(self):
        # email = self.cleaned_data.get("email")
        lista_de_erros = {}

        # email_not_dcx(email, 'email', lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_error = lista_de_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data


class DateInput(forms.DateInput):
    input_type = 'date'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        labels = {'nome': 'Nome', 'idade': 'Idade',
                  'matricula': 'Matricula', 'data_ingresso': 'Data de Ingresso', 'data_estimada_saida': 'Data Estimada saida', 'periodo': 'Período ', 'cra': 'CRA', 'curso': 'Seu curso', 'nota_introducao': 'Nota Introdução Prog', 'nota_POO': 'Nota POO', 'nota_linguagem': 'Nota Linguagem Prog', 'nota_estrutura': 'Nota Estrutura Dados', 'disposicao': 'Disponibilidade 20 Horas', 'numero_disciplinas': 'Número disciplinas Periodo', 'link_git_hub': 'Link GITHUB', 'link_linkedin': 'Link Linkedin'}
        widgets = {
            'user': forms.HiddenInput,
            # 'data_ingresso': forms.widgets.DateInput(attrs={'type': 'date'}),
            # 'data_estimada_saida': DateInput()
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
            'cra':  mark_safe(
                '<ul class="listError">\
                    <li>Coloque valores possitivos e dentro do escopo de 0 a 10</li>\
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
            'nota_introducao': mark_safe(
                '<ul class="listError">\
                    <li>Coloque sua nota na cadeira de Introdução a Programação</li>\
                    <li>Este campo não pode ser vázio</li>\
                    <li>Colocar uma nota entre 0 e 10</li>\
                <ul/>'
            ),
            'nota_POO': mark_safe(
                '<ul class="listError">\
                    <li>Coloque sua nota na cadeira de Programação orientada a objetos</li>\
                    <li>Caso não tenha cursado pode deixar vazio</li>\
                    <li>Colocar uma nota entre 0 e 10</li>\
                <ul/>'
            ),
            'nota_linguagem':  mark_safe(
                '<ul class="listError">\
                    <li>Coloque sua nota na cadeira de Linguagem de programação</li>\
                    <li>Caso não tenha cursado pode deixar vazio</li>\
                    <li>Colocar uma nota entre 0 e 10</li>\
                <ul/>'
            ),
            'nota_estrutura': mark_safe(
                '<ul class="listError">\
                    <li>Coloque sua nota na cadeira de Estrutua de dados</li>\
                    <li>Caso não tenha cursado pode deixar vazio</li>\
                    <li>Colocar uma nota entre 0 e 10</li>\
                <ul/>'
            ),
            'disposicao': mark_safe(
                '<ul class="listError">\
                    <li>Coloque sim caso tenha 20 horas semanais disponiveis exclusivamente para o projeto</li>\
                    <li>Este campo não pode ficar vazio</li>\
                <ul/>'
            ),
            'numero_disciplinas': mark_safe(
                '<ul class="listError">\
                    <li>Coloque o número de disciplinas que está cursando esse semestre</li>\
                    <li>Este campo só aceita valores possítivos</li>\
                    <li>Este campo não pode ficar vazio</li>\
                <ul/>'
            ),
            'link_git_hub': mark_safe(
                '<ul class="listError">\
                    <li>Coloque o link do seu GITHUB</li>\
                    <li>Este campo pode ficar vazio</li>\
                <ul/>'
            ),
            'link_linkedin':  mark_safe(
                '<ul class="listError">\
                    <li>Coloque o link do seu Linkedin</li>\
                    <li>Este campo pode ficar vazio</li>\
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
        curso = self.cleaned_data.get("curso")
        nota_introducao = self.cleaned_data.get("nota_introducao")
        nota_POO = self.cleaned_data.get("nota_POO")
        nota_linguagem = self.cleaned_data.get("nota_linguagem")
        nota_estrutura = self.cleaned_data.get('nota_estrutura')
        disposicao = self.cleaned_data.get('disposicao')
        numero_disciplinas = self.cleaned_data.get('numero_disciplinas')

        lista_de_erros = {}

        nome_invalid(nome, user, 'nome', lista_de_erros)
        matricula_invalid(matricula, user, 'matricula', lista_de_erros)
        periodo_invalid(periodo, 'periodo', lista_de_erros)
        cra_invalid(cra, 'cra', lista_de_erros)
        date_in_invalid(data_ingresso, data_saida,
                        'data_ingresso', lista_de_erros)
        curso_invalid(curso, 'curso', lista_de_erros)
        nota_introducao_invalid(
            nota_introducao, 'nota_introducao', lista_de_erros)
        nota_POO_invalid(nota_POO, 'nota_POO', lista_de_erros)
        nota_linguagem_invalid(
            nota_linguagem, 'nota_linguagem', lista_de_erros)
        nota_estrutura_invalid(
            nota_estrutura, 'nota_estrutura', lista_de_erros)
        disposicao_invalid(disposicao, 'disposicao', lista_de_erros)
        numero_disciplinas_invalid(
            numero_disciplinas, 'numero_disciplinas', lista_de_erros)

        # print(lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_error = lista_de_erros[erro]
                self.add_error(erro, mensagem_error)

        return self.cleaned_data
