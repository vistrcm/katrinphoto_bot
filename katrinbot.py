import logging
from flask import Flask

app = Flask(__name__)
app.config.from_object('katrinbot_settings')
URL = "https://vitko.info/katrinphotobot/wh/"
WH_URL = app.config['URL'] + app.config['TOKEN']


@app.route("/")
def index():
    return "index page"


@app.route("/wh/%s" % app.config['TOKEN'])
def webhook():
    app.logger.debug("got message")
    return "ok"


def register_webhook():
    return "hh"

if __name__ == "__main__":
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        ch = logging.StreamHandler()
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        app.logger.addHandler(ch)
        app.logger.setLevel(logging.INFO)
    app.run()
