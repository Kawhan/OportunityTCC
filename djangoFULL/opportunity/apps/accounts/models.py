from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(("date joined"), default=timezone.now)
    first_name = models.CharField(("first name"), max_length=150, blank=True)
    last_name = models.CharField(("last name"), max_length=150, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    verify_staff_user = models.BooleanField(default=False)
    user_is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    resp = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    curso = (
        ('SI', 'Sistemas de Informação'),
        ('LCC', 'Lic. Ciência da Computação')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=True, blank=True, unique=True)
    idade = models.IntegerField(null=True, blank=True)
    matricula = models.CharField(
        unique=True, max_length=11, null=True, blank=True)
    data_ingresso = models.DateField(null=True, blank=True)
    data_estimada_saida = models.DateField(null=True, blank=True)
    periodo = models.IntegerField(null=True, blank=True)
    cra = models.FloatField(null=True, blank=True)
    curso = models.CharField(max_length=3, null=True,
                             blank=True, choices=curso)
    nota_introducao = models.IntegerField(null=True, blank=True)
    nota_POO = models.IntegerField(null=True, blank=True)
    nota_linguagem = models.IntegerField(null=True, blank=True)
    nota_estrutura = models.IntegerField(null=True, blank=True)
    disposicao = models.CharField(
        max_length=1, null=True, blank=True, choices=resp)
    numero_disciplinas = models.IntegerField(null=True, blank=True)
    link_git_hub = models.CharField(max_length=255, null=True, blank=True)
    link_linkedin = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('nome', 'matricula',)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
