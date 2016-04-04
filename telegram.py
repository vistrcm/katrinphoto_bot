import logging
import requests


logger = logging.getLogger(__name__)


class Bot(object):
    def __init__(self, token):
        self.__token = token
        self.__bot_url = "https://api.telegram.org/bot{bottoken}".format(bottoken=self.__token)

    def __send_request(self, method_name, payload):
        uri = "{bot_url}/{method_name}".format(bot_url=self.__bot_url, method_name=method_name)
        r = requests.post(uri, json=payload)
        return r.json()

    def send_message(self, chat_id, text, reply_to_message_id=None, reply_markup=None):
        logger.warn("sending message to %s", chat_id)
        payload = {
            "chat_id": chat_id,
            "text": text,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        }
        return self.__send_request("sendMessage", payload)

    def register_webhook(self, url):
        logger.info("Trying to unregister webhook")
        logger.info(self.__send_request("setWebhook", {"url": ""}))
        logger.info("Setting webhook to: %s" % url)
        return self.__send_request("setWebhook", {"url": url})
