from django.core.mail import send_mail
import uuid
from django.conf import settings
from django.template.loader import render_to_string
from authentication.models import Org


def send_password_mail(email, token, user):
    subject = "Please Set Your Password and Active Your Account"
    org = Org(user=user)
    message = render_to_string(
        'orgmail/activate.html', {"token": token, "org": org})
    email_from = settings.EMAIL_HOST_USER
    recpipient_list = [email]
    send_mail(subject, message, email_from, recpipient_list)


def send_success_mail(email, user):
    subject = "Thank Your Account Is Successfully Activated"
    org = Org(user=user)
    message = render_to_string(
        'orgmail/success.html', {"org": org})
    email_from = settings.EMAIL_HOST_USER
    recpipient_list = [email]
    send_mail(subject, message, email_from, recpipient_list)
