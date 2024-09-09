from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

# Señal para crear o actualizar automáticamente el perfil cuando un usuario es creado
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
