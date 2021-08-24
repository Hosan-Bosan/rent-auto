from django.core.mail import send_mail


def send_activation_code(email, activation_code, status):
    if status == 'register':
        url = f'http://localhost:7800/api/v1/account/activate/{activation_code}'
        message = f'Нажмите на эту ссылку для активации аккаунта{url}'
        send_mail(
            'Активируйте ваш аккаунт',
            message,
            'aman@gmail.com',
            [email, ],
            fail_silently=False
        )
