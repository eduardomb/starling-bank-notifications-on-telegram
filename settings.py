from os import environ

TELEGRAM_TOKEN = environ.get('TELEGRAM_TOKEN', default=None)
TELEGRAM_CHATID = environ.get('TELEGRAM_CHATID', default=None)
STARLING_WEBHOOK_SECRET = str.encode(
    environ.get('STARLING_WEBHOOK_SECRET', default=None)
)

if not TELEGRAM_TOKEN:
    raise ValueError('No TELEGRAM_TOKEN set for Flask application')

if not TELEGRAM_CHATID:
    raise ValueError('No TELEGRAM_CHATID set for Flask application')

if not STARLING_WEBHOOK_SECRET:
    raise ValueError('No STARLING_WEBHOOK_SECRET set for Flask application')
