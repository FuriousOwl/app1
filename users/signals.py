from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile
from therapists.models import TherapistProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff:
            TherapistProfile.objects.create(user=instance)
        else:
            UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
    if hasattr(instance, 'therapistprofile'):
        instance.therapistprofile.save()