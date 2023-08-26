# your_app/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_registration_email(user_email):
    subject = 'Registration Successful'
    message = 'Thank you for registering!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print('Email sent successfully')
    except Exception as e:
        print('Email sending failed:', e)
