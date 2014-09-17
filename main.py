"""`main` is the top level module for your Flask application."""

from __future__ import absolute_import, division, print_function

import logging

from flask import Flask, request

from message import Message
from bots.daniel import Daniel

app = Flask(__name__)


@app.route('/daniel', methods=['POST'])
def daniel():
    msg = Message.parse(request)
    logging.debug(msg)
    if msg.user_name == "slackbot":
        return ''
    bot = Daniel(msg)
    return bot.say()

