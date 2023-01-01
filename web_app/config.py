import os
from dotenv import load_dotenv


load_dotenv()

class Config():
    WTF_CSRF_SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Recaptcha Security
    RECAPTCHA_PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
    RECAPTCHA_VERIFY_SERVER = "https://www.google.com/recaptcha/api/siteverify"
    RECAPTCHA_PARAMETERS = {'render': 'explicit'}
    RECAPTCHA_DATA_ATTRS = {'theme': 'light'}
