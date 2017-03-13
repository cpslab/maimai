#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
from contextlib import closing
import xml.etree.ElementTree as ET
import time
import requests
import os
import sys
sys.path.append("/home/pi")

# TODO what?
time.sleep(5)

# say
import subprocess
from os import path
import glob
import importlib

class Bot(object):
    def __init__(self):
        self._command = ''
        self._listeners = self._load_scripts()

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value

    def say(self, message):
        shutup()
        print('bot >: ' +  message)
        subprocess.Popen([python3_path, akane_path, message, "2.0", "1.4", "1.0", "1.0"])
    def listen(self, message):
        for listener in self._listeners:
            try:
                listener.main(self)
            except Exception as e:
                print(e)

    def _load_scripts():
        listeners = []
        for f in glob.glob('scripts/*.py'):
            moduleName = path.splitext(path.basename(f))[0]
            if (moduleName == '__init__'):
                continue
            module = importlib.import_module('scripts.' + moduleName)
            if callable(module.main):
                listeners.append(module)
        return listeners

    def stop_say(self):
        home_path = os.environ['HOME']
        killaudio_path = os.path.join(home_path, 'killaudio')
        subprocess.Popen(['sh', killaudio_path])

home_path = '/home/pi/'
akane_path = '/home/pi/akane-chan/main.py'

def shutup():
    killaudio_path = home_path + 'killaudio'
    subprocess.Popen(['sh', killaudio_path])

def say(message):
    shutup()
    print('echo >: ' +  message)
    # voice_process = subprocess.Popen([python3_path, akane_path] + message.split(), stdout=subprocess.PIPE)
    subprocess.Popen(['/usr/bin/python3', akane_path, message, "2.0", "1.4", "1.0", "1.0"])
    return 'message: ' + message

def run_weather():
    print('weather')
    p = subprocess.Popen(['cat', weather_cache_path], stdout=subprocess.PIPE)
    p.wait()
    stdout_data = p.stdout.read()
    say(stdout_data)

def commands_loop(root):
    for word in root.iter('WHYPO'):
        command = word.get('WORD')
        cm = float(word.get('CM'))
        print()
        print(command + ": [" + str(cm) + "]")
        if cm < 0.50:
            print('skip')
            continue
        if command == 'shutup' and cm > 0.90:
            shutup()
        elif command == 'start':
            if cm <= 0.94:
                continue
            is_state_recieve = True
            say('はい')
            break
        elif is_state_recieve:
            if cm < 0.94:
                say('え？')
                break
            else:
                bot.listen(command)
                is_state_recieve = False

def main():
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    text_queue = ""
    separator = ".\n"
    is_state_recieve = False

    bot = Bot()

    say('まいまい起動しました')

    while True:
        recv_data = sock.recv(bufsize)

        # print (recv_data)
        # parser.feed(recv_data)
        text_queue += recv_data
        if separator in text_queue:
            parts = text_queue.split(separator)
            xmls, text_queue = parts[:-1], parts[-1]
            # print(xmls)
            print(".", end="")
            # 前回受け取ったコマンドが 'start' であるか
            for xml_text in xmls:
                try:
                    root = ET.fromstring(xml_text)
                    commands_loop(root)
                except ET.ParseError:
                    print()
                    print('parce error--')
                    print(xml_text)
                    print('--')

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        bot.listen('exit')
