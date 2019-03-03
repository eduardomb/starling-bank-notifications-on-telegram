from flask import Flask, request, abort

from telegram_bot import ChatSession

app = Flask(__name__)
app.config.from_object('settings')

@app.route('/starling', methods=['POST'])
def starling():
    def has_valid_signature():
        # FIXME
        return True

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
