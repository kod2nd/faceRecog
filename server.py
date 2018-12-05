#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:49:47 2018

@author: zhenhao
"""

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import logging
import process

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

#@socketio.on_connect()
#def connected():
#    emit('hello')
    
#
@socketio.on('my event', namespace='/test')
def test_message(message):
    print('test')
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    logger.info('testing')
#    with open('logging.txt', 'w+') as f:
#        f.write(str(message['data']))
    
    pred=process.main(message['data'])
        
    emit('my response', {'data': pred}, broadcast=True)


if __name__ == '__main__':
    logger.info('Running socket IO')
    socketio.run(app, host='localhost', port=8080)
