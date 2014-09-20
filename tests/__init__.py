# coding: utf-8

from __future__ import absolute_import, division, print_function

import logging 

from src import main


logging.basicConfig(level=logging.DEBUG)

def fetch(uri, params):
    default = {
        "token": "o9bMTLDgQe7LPBQvPnw0h0uS",
        "team_id": "T0001",
        "channel_id": "C2147483705",
        "channel_name": "test",
        "timestamp": "1355517523.000005",
        "user_id": "U2147483697",
        "user_name": "Steve",
        "text": "googlebot: What is the air-speed",
        "trigger_word": "googlebot:",
    }
    default.update(params)
    app = main.app.test_client()
    result = app.post(uri, data=default)
    logging.info(result.status)
    logging.info(result.data)
    return result
