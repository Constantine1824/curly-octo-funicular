from .utils import UrlSign
from .models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .email import SendMails

@receiver(post_save, sender=User)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        SendMails().send_verification_mail(user=instance)
        