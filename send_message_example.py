from argparse import ArgumentParser
from telegram_bot import ChatSession

parser = ArgumentParser(description='Send a message to a telegram user.')
parser.add_argument(
    '--telegram-token',
    type=str,
    required=True,
    help='Telegram Bot Token'
)
parser.add_argument(
    '--telegram-chatid',
    type=str,
    required=True,
    help='Telegram Chat ID'
)
args = parser.parse_args()
chat = ChatSession(args.telegram_token, args.telegram_chatid)
chat.send_message('Hello')
