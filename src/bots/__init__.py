# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging 

from flask import jsonify
import types


class BaseBot(object):

    _ICON = ":slack:"
    _NAME = "Slack"

    def __init__(self, msg):
        self.msg = msg

    def say(self):
        # 関数を探す
        for key in dir(self):
            if key.startswith("_") or key == "say":
                continue
            attr = getattr(self, key)
            # logging.debug(key + " type" + str(type(attr)))
            if not isinstance(attr, types.MethodType):
                continue

            # 実行してみて結果があれば返す
            logging.debug("execute:" + key + "()")
            result = attr()
            if result:
                return jsonify({
                    "text": result,
                    "username": self._NAME,
                    "icon_emoji": self._ICON
                })
        return ""

