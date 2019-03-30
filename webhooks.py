from hmac import compare_digest
from base64 import b64encode
from hashlib import sha512

from flask import Flask, request, abort

from telegram_bot import ChatSession

app = Flask(__name__)
app.config.from_envvar('ALERT_BOT_SETTINGS')

@app.route('/starling', methods=['POST'])
def starling():
    def has_valid_signature():
        header_signature = request.headers.get('X-Hook-Signature')

        if not header_signature:
            return False

        m = sha512()
        m.update(app.config['STARLING_WEBHOOK_SECRET'])
        m.update(request.get_data())
        expected_signature = b64encode(m.digest()).decode()

        return compare_digest(header_signature, expected_signature)

    if not has_valid_signature():
        abort(400)

    msg = request.json.get('content', {}).get('forCustomer', None)

    if msg:
        chat = ChatSession(
            app.config['TELEGRAM_TOKEN'],
            app.config['TELEGRAM_CHATID']
        )
        chat.send_message(msg)

    return ''
