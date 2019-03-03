from requests import post

__all__ = ['ChatSession']

class ChatSession:
    _API_URI = 'https://api.telegram.org/bot{token}/{command}'

    def __init__(self, token, chat_id):
        '''
        Instantiate a ChatSession with a specific user.
        - To obtain the token use the BotFather bot on Telegram
          (https://t.me/botfather). You can either create a new bot or obtain
          the token for an existing one.
        - To obtain chat_id for a specific user, follow these steps:
            1. Start a conversation with your bot, and send it any message.
            2. Run "curl https://api.telegram.org/bot$TOKEN/getUpdates" on the
            shell and look for the chat id.
        '''
        self.token = token
        self.chat_id = chat_id

    def send_message(self, plain_text):
        payload = {'chat_id': self.chat_id, 'text': plain_text}
        res = self._api_request('sendMessage', payload)

    def _api_request(self, command, payload):
        uri = self._API_URI.format(token=self.token, command=command)
        return post(uri, data=payload)
