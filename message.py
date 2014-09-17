# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging


class Message(object):
    token = ""
    team_id = ""
    channel_id = ""
    channel_name = ""
    timestamp = 0
    user_id = ""
    user_name = ""
    # raw text
    text = ""
    # parsed text
    args = []
    command = ""
    trigger_word = ""

    @classmethod
    def parse(cls, request):
        params = request.form
        msg = cls()
        try:
            msg.team_id = params["team_id"]
            msg.channel_id = params["channel_id"]
            msg.channel_name = params["channel_name"]
            msg.timestamp = params["timestamp"]
            msg.user_id = params["user_id"]
            msg.user_name = params["user_name"]
            msg.text = params["text"]
            msg.trigger_word = params["trigger_word"]

            msg.args = msg.text.split()
            logging.debug(msg.args)
            if len(msg.args) >= 2:
                msg.command = msg.args[1]
        except Exception, e:
            logging.error(e)
        return msg

    def __str__(self):
        res = self.__class__.__name__
        res += "@{0.token}[channel={0.channel_name}, user={0.user_name}, text={0.text}]".format(self)
        return res
