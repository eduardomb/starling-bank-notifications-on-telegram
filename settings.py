import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', default=None)
TELEGRAM_CHATID = os.environ.get('TELEGRAM_CHATID', default=None)

if not TELEGRAM_TOKEN:
    raise ValueError('No TELEGRAM_TOKEN set for Flask application')

if not TELEGRAM_CHATID:
    raise ValueError('No TELEGRAM_CHATID set for Flask application')
