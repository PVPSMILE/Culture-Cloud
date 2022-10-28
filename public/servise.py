from django.core.mail import send_mail

def send(user_email):
    send_mail(
        "Hello from Culture Cloud at know you joined to our family",
        "woooooow",
        'frank01zeroy@gmail.com',
        [user_email],
        fail_silently=False
    )