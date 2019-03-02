from flask import Flask

app = Flask(__name__)

@app.route('/webhooks/starling')
def starling_webhook():
    return 'Success'
