import requests
import urllib
import json


class Telegram:

    def __init__(self, token):
        self.TOKEN = token

    @property
    def TELEGRAM_URL(self):
        return f"https://api.telegram.org/bot{self.TOKEN}/"

    def __api_endpoint(self, url):
        if urllib.parse.urlparse(url).scheme in ['http', 'https']:
            return url  # url is already complete
        return urllib.parse.urljoin(f'{self.TELEGRAM_URL}/',
                                    url.lstrip('/'))

    def getMe(self):
        """
        Obtém as principais informações do bot

        :return: JSON com as informações do bot
        """
        return json.loads(requests.get(self.__api_endpoint('getMe')).text)

    def getUpdates(self):
        """
        Obtém as atualizações de chat do bot

        :return: JSON com os dados dos chats
        """
        return json.loads(requests.get(self.__api_endpoint('getUpdates')).text)

    def getChat(self, chat_id):
        """
        Obtém as informações do chat pelo ID

        :param int chat_id: ID do chat
        :return: JSON com os dados do chat
        """
        return json.loads(requests.post(self.__api_endpoint('getChat'),
                                        headers={'Content-Type': 'application/json'},
                                        json={'chat_id': chat_id}).text)

    def sendMessage(self, chat_id, message):
        """
        Envia a mensagem para um chat ou grupo

        :param chat_id: ID do chat ou grupo
        :param message: Mensagem a ser enviada
        :return:
        """
        return json.loads(requests.post(self.__api_endpoint('sendMessage'),
                                        headers={'Content-Type': 'application/json'},
                                        json={'chat_id': chat_id, 'text': message}).text)
