from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    location = CountryField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
# Define signals so that the Profile model will be automatically created/updated
# when User instances are created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
