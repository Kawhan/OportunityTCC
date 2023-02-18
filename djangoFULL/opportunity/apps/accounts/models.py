from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    matricula = models.CharField(
        unique=True, max_length=11, null=True, blank=True)
    data_ingresso = models.DateField(null=True, blank=True)
    data_estimada_saida = models.DateField(null=True, blank=True)
    periodo = models.IntegerField(null=True, blank=True)
    cra = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
