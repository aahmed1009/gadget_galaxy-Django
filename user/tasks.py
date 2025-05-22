from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_verification_email(email, uid, token):
    link = f"http://127.0.0.1:8000/activate/{uid}/{token}/"
    subject = "Activate Your Account"
    message = f"Click this link to activate your account:\n{link}"
    send_mail(subject, message, 'noreply@example.com', [email])
