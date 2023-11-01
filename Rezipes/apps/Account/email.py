from threading import Thread
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import threading
from .utils import UrlSign
from django.conf import settings

class EmailThread:
    
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class SendMails:

    def send_verification_mail(self, user):
        subject = 'Activate your account'
        url = UrlSign().url_encode(username=user.username)
        complete_url :str #Initialize complete url to bypass any local unbound error
        if settings.BASE_URL:
            complete_url = settings.BASE_URL/url
        else:
            complete_url = f'127.0.0.1:8000/auth/verify/{url}'
        message = render_to_string(
            'activation.html',
            {
                'url' : complete_url
            }
        )
        email = EmailMessage(subject,message, to=[user.email])
        email.content_subtype = 'html'
        EmailThread(email).run()

    def send_password_reset_mail(self):
        pass