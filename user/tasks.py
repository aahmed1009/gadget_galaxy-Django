from django.core.mail import send_mail

from django.conf import settings

from django.template.loader import render_to_string

from celery import shared_task


@shared_task
def send_verification_email(email, uid, token):
    subject = 'Activate your account'
    activation_link = f'http://127.0.0.1:8000/activate/{uid}/{token}/'

    message = render_to_string('activation_email.html', {
        'activation_link': activation_link
    })

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])