import datetime

from accounts.decorators import user_not_authenticated
from accounts.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from accounts.models import User, UserProfile
from accounts.tokens import account_activation_token
from django.contrib import auth, messages
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sites.shortcuts import get_current_site
# Email
from django.core.mail import EmailMessage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request, "Obrigado pela sua confirmação por e-mail. Agora você pode acessar sua conta.")
        return redirect('login')
    else:
        messages.error(request, "O link de ativação é inválido!")

    return redirect('index')


def activateEmail(request, user, to_email):
    mail_subject = "Ative sua conta."
    context = {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    }
    message = get_template('template_activate_account.html').render(context)
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = "html"
    if email.send():
        messages.success(request, f'Prezado {user}, vá até a caixa de entrada do seu e-mail {to_email} e clique em \
                recebeu o link de ativação para confirmar e concluir o registro. Observação: verifique sua pasta de spam.')
    else:
        messages.error(
            request, f'Problema ao enviar e-mail para {to_email}, verifique se você digitou corretamente.')


@user_not_authenticated
def cadastro(request):
    # form = UserRegistrationForm()

    dados = {}

    dados["title"] = "Registro"
    user_profile_form = UserRegistrationForm()
    dados["form"] = user_profile_form

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('index')

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'Este campo é obrigatório.':
                    messages.error(
                        request, "Você deve fazer o teste de reCAPTCHA")

        dados["form"] = form

    return render(
        request,
        "accounts/register.html",
        dados,
    )


def login(request):
    form = UserLoginForm()

    dados = {}

    dados['title'] = "Login"
    dados['form'] = form

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                auth.login(request, user)
                dados = {}
                dados["title"] = "Cadastro Informacoes"

                if user.user_is_teacher:
                    dados['title'] = 'Home'
                    messages.success(
                        request, "Login realizado com sucesso! Seja bem-vindo Professor(a)")
                    return redirect('index')

                aluno = get_object_or_404(UserProfile, pk=user.id)

                if aluno.is_verify:
                    messages.success(
                        request, "Login realizado com sucesso! Seja bem vindo")
                    return redirect('index')

                messages.success(
                    request, "Login realizado com sucesso! Cadastre suas informações!")

                return redirect('profile')
            else:
                messages.error(request, 'Credenciais invalidas!.')
                return redirect('login')

        # else:
        #     for key, error in list(form.errors.items()):
        #         if key == 'captcha' and error[0] == 'Este campo é obrigatório.':
        #             messages.error(
        #                 request, "Você deve fazer o teste de reCAPTCHA")

        messages.error(
            request, "Dados incorretos, por favor tente verificar as informações digitadas!")
        dados["form"] = form

    return render(request, 'accounts/login.html', dados)


# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         senha = request.POST['senha']

#         if not email.strip():
#             messages.error(request, "O campo email não pode ficar em branco")
#             return redirect('login')

#         if not senha.strip():
#             messages.error(request, "Senha vazia!")
#             return redirect('login')

#         # Trazendo as informações desse usuário apartir do email
#         if User.objects.filter(email=email).exists():
#             user = auth.authenticate(request, email=email, password=senha)

#             if user == None:
#                 messages.error(
#                     request, 'Cedenciais invalidas.')
#                 return redirect('login')

#             if not user.is_active:
#                 messages.error(
#                     request, 'Confirme seu e-mail para continuar.')
#                 return redirect('login')
#             if user is not None:
#                 auth.login(request, user)
#                 dados = {}
#                 dados["title"] = "Cadastro Informacoes"

#                 if user.user_is_teacher:
#                     dados['title'] = 'Home'
#                     messages.success(
#                         request, "Login realizado com sucesso! Seja bem-vindo Professor(a)")
#                     return redirect('index')

#                 messages.success(
#                     request, "Login realizado com sucesso! Cadastre suas informações")
#                 return redirect('profile')
#             else:
#                 messages.error(request, 'Credenciais invalidas!.')
#                 return redirect('login')
#         else:
#             messages.error(request, 'Credenciais invalidas!.')
#             return redirect('login')
#     else:
#         dados = {}
#         dados["title"] = "Login"
#         if not request.user.is_authenticated:
#             return render(request, 'accounts/login.html', dados)
#         else:
#             messages.error(
#                 request, 'Você já está logado! Por favor efetue o logout.')
#             return redirect('index')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!.')
    return redirect('index')


@login_required
@transaction.atomic
def update_profile(request):
    dados = {}

    dados["title"] = "Cadastro de informacoes"

    user_profile_form = UserProfileForm(instance=request.user.userprofile)
    dados["form"] = user_profile_form

    if request.method == "POST":
        user_profile_form = UserProfileForm(
            request.POST, instance=request.user.userprofile)

        if user_profile_form.is_valid():
            aluno = user_profile_form.save(commit=False)
            aluno.is_verify = True
            messages.success(
                request, "Obrigado por cadastrar suas informações!")
            user_profile_form.save()
            return redirect('index')
        # else:
        #     for error in list(user_profile_form.errors.values()):
        #         messages.error(request, error)

        dados["form"] = user_profile_form

    return render(request, 'accounts/profile.html', dados)
