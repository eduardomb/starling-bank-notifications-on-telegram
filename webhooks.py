from flask import Flask

app = Flask(__name__)

@app.route('/starling')
def starling():
    return 'Success'
