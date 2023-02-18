from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render


def login(request):
    dados = {}

    dados['title'] = "Login"
    return render(request, 'accounts/login.html', dados)


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        # Validando se o nome é null
        if not nome.strip():
            messages.error(request, "O nome não pode ficar em branco")
            return redirect('cadastro')

        if not email.strip():
            messages.error(request, "O email não pode ficar em branco")
            return redirect('cadastro')

        # Validando se o campo de email não esta em branco
        if not nome.strip():
            messages.error(request, "O campo nome não pode ficar em branco")
            return redirect('cadastro')

        # Validando senha
        if senha != senha2:
            messages.error(request, "As senhas não são iguais!")
            return redirect('cadastro')

        # Verificar se o usuário que queremos criar está na base de dados
        if User.objects.filter(email=email).exists():
            messages.error(request, "Usuario já cadastrado")
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, "Usuario já cadastrado")
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email, password=senha)

        user.save()
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')
    else:
        dados = {}
        dados["title"] = "Cadastro"
        return render(request, 'accounts/cadastro.html', dados)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if not email.strip():
            messages.error(request, "O campo email não pode ficar em branco")
            return redirect('login')

        if not senha.strip():
            messages.error(request, "Senha vazia!")
            return redirect('login')

        # Trazendo as informações desse usuário apartir do email
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()

            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                dados = {}
                dados["title"] = "Home"
                messages.success(
                    request, "Login realizado com sucesso! Cadastre suas informações")
                return redirect('profile')
            else:
                messages.error(request, 'Credenciais invalidas!.')
                return redirect('login')
        else:
            messages.error(request, 'Credenciais invalidas!.')
            return redirect('login')
    else:
        dados = {}
        dados["title"] = "Login"
        if not request.user.is_authenticated:
            return render(request, 'accounts/login.html', dados)
        else:
            messages.error(
                request, 'Você já está logado! Por favor efetue o logout.')
            return redirect('index')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!.')
    return redirect('index')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_profile_form = UserProfileForm(
            request.POST, instance=request.user.userprofile)

        if user_profile_form.is_valid():
            messages.success(
                request, "Obrigado por cadastrar suas informações!")
            user_profile_form.save()
            return redirect('index')
    else:
        dados = {}

        dados["title"] = "cadastro de informacoes"
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
        dados["form"] = user_profile_form
    return render(request, 'accounts/profile.html', dados)


@login_required
@transaction.atomic
def update_profile_2(request):
    if request.method == 'POST':
        pass
    else:
        user_profile_form = get_object_or_404(UserProfile, pk=request.user.id)
        dados = {}

        dados["title"] = "cadastro de informacoes"
        dados["form"] = user_profile_form
        return render(request, 'accounts/profile_2.html', dados)
