import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'msdn_club_usf'

# captcha config
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6Lc7KfwSAAAAAO2ewgfog50aM8yr8RpPzrQNsg_e'
RECAPTCHA_PRIVATE_KEY = '6Lc7KfwSAAAAAPUFrcSIZgbYWaAlDyXN7EfXZFqT'
RECAPTCHA_OPTIONS = {'theme': 'white'}

UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
ALLOWED_EXTENSIONS = set(['cs', 'py', 'cpp', 'java'])