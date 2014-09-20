"""`main` is the top level module for your Flask application."""

from __future__ import absolute_import, division, print_function

import logging

from flask import Flask, request

from .message import Message
from .bots.daniel import Daniel

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ dummy page for checking that Flask is running"""
    return "Hello Python Slack Bot"


@app.route('/daniel', methods=['POST'])
def daniel():
    """Daniel is a BOT, who reacts with calling his name
    1) yo
    you: daniel yo
    daniel: yo

    2) echo
    you: daniel echo HelloWorld
    daniel: HelloWorld
    """
    msg = Message.parse(request)
    logging.debug(msg)
    # prevents infinite loop
    if msg.user_name == "slackbot":
        return ''
    bot = Daniel(msg)
    return bot.say()

