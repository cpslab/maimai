#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
from contextlib import closing
import xml.etree.ElementTree as ET
import time
import os
import sys
from os import path
from bot import Bot

# TODO
sys.path.append("/home/pi")

# TODO what?
time.sleep(5)

home_path = '/home/pi'

bot = Bot()
is_state_recieve = False

def main():
    host = 'localhost'
    port = 10500
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    text_queue = ""
    separator = ".\n"

    bot.say('まいまい起動しました')

    while True:
        bufsize = 4096
        recv_data = sock.recv(4096)
        text_queue += recv_data.decode('utf-8')
        if separator in text_queue:
            parts = text_queue.split(separator)
            xmls, text_queue = parts[:-1], parts[-1]
            print(".", end="")
            search_xmls(xmls)

def search_xmls(xmls):
    for xml_text in xmls:
        try:
            root = ET.fromstring(xml_text)
            dispatch_command(root)
        except ET.ParseError:
            print()
            print('parce error--')
            print(xml_text)
            print('--')

def dispatch_command(root):
    global is_state_recieve
    for word in root.iter('WHYPO'):
        command = word.get('WORD')
        cm = float(word.get('CM'))
        print()
        print(command + ": [" + str(cm) + "]")
        if cm < 0.50:
            print('skip')
            continue
        if command == 'shutup' and cm > 0.90:
            bot.stop_say()
        # 前回受け取ったコマンドが 'start' であるか
        elif command == 'start':
            if cm <= 0.94:
                continue
            is_state_recieve = True
            bot.say('はい')
            break
        elif is_state_recieve:
            if cm < 0.94:
                bot.say('え？')
                break
            else:
                print('>>>' + command)
                bot.listen(command)
                is_state_recieve = False

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        # bot.listen('exit')
