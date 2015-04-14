#!/usr/bin/python
#-*- coding: utf-8 -*-

import twitter
import io
import json

#Funcion para la conexion.
def oauth_login():
    CONSUMER_KEY = 'IGnkagX2BIVJSg3GwmNWAiWuK'
    CONSUMER_SECRET = 'WAPs5AUCHG0SqRu80InstXJ6CZ94qBsdpXwmtxITC4gQDVZeiD'
    OAUTH_TOKEN = '14198458-cmPMWBFGN7dvjfFa4VDQFPkZFwPBn5BwL6uSY6w4O'
    OAUTH_TOKEN_SECRET = 'GzJeF4AhX3KtsXUa8CJwUkt2mvWennBKKdzNIdvN4zjzl'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Funcion para grabar la informacion en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Funcion para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()
