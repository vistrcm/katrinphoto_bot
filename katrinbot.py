# -*- coding: utf-8 -*-
import logging

from flask import Flask
from flask import jsonify
from flask import request

from siteworker import get_latest, get_random
from telegram import Bot

app = Flask(__name__)
app.config.from_object('katrinbot_settings')
URL = "https://vitko.info/katrinphotobot/wh/"
WH_URL = app.config['URL'] + app.config['TOKEN']

bot = Bot(app.config['BOT_TOKEN'])


@app.route("/")
def index():
    return "index page"


def processwh(msg):
    repl_url = "http://lene.pois.org.ru/Katrin/img/{}"

    chat = msg["message"]["chat"]
    message_id = msg["message"]["message_id"]
    text = msg["message"].get("text", None)

    if text is not None:
        if text in ["/start", "/help"]:
            response = "Используй команды /random или /latest."
        elif text.startswith("/latest"):
            item = get_latest()
            response = repl_url.format(item)
        elif text.startswith("/random"):
            item = get_random()
            response = repl_url.format(item)
        else:
            response = "Шо?"

        # set keyboard
        if chat["type"] == "private":
            reply_markup = {"keyboard": [["/latest"], ["/random"]]}
        else:
            reply_markup = None

        bot.send_message(chat["id"], response, reply_markup=reply_markup)
    else:
        response = "No text in the message."
    return response


@app.route("/wh/%s" % app.config['TOKEN'], methods=['GET', 'POST'])
def webhook():
    app.logger.debug("got message")
    if request.method == 'POST':
        msg = request.get_json()
        app.logger.debug(msg)
        answer = processwh(msg)
        return jsonify(status="ok", answer=answer)
    else:
        return jsonify(status="ok")


if __name__ == "__main__":
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        ch = logging.StreamHandler()
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        app.logger.addHandler(ch)
        app.logger.setLevel(logging.DEBUG)
    wh_result = bot.register_webhook(WH_URL)
    app.logger.debug(wh_result)
    app.run()
