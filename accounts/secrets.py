class Secrets:
    def __init__(self) -> None:
        pass

    # EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" #for console debugging
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465 #587 default
    MAIL_USERNAME='mymail@gmail.com' #Replace with your mail
    MAIL_PASSWORD='my password' #Replace with your password
    MAIL_USE_TLS= False
    MAIL_USE_SSL=True