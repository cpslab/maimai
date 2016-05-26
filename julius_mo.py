# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import socket
from contextlib import closing
import commands
import xml.etree.ElementTree as ET
import datetime

# say
import subprocess
from flask import Flask
app = Flask(__name__)

home_path = '/home/pi/'
aques_path = home_path + 'speak_api/lib/aquestalkpi/AquesTalkPi'
absolute_script_path = home_path + 'run_duo.py'

def say(message):
    print('echo >: ' +  message)
    voice_process = subprocess.Popen([aques_path] + message.split(), stdout=subprocess.PIPE)
    subprocess.Popen(['aplay'], stdin=voice_process.stdout)
    return 'message: ' + message

def run_absolute():
    print('absolute')
    subprocess.Popen(['python2', absolute_script_path])

def main():
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    text_queue = ""
    separator = ".\n"
    is_state_recieve = False

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
                    for word in root.iter('WHYPO'):
                        command = word.get('WORD')
                        cm = float(word.get('CM'))
                        print()
                        print(command + ": [" + str(cm) + "]")
                        if cm < 0.50:
                            print('skip')
                            continue
                        if command == 'start':
                            if cm <= 0.94 or is_state_recieve:
                                continue
                            is_state_recieve = True
                            say('はい')
                            break
                        elif is_state_recieve:
                            if cm < 0.80:
                                say('え？')
                                break
                            else:
                                start(command)
                                is_state_recieve = False
                except ET.ParseError:
                    print()
                    print('parce error--')
                    print(xml_text)
                    print('--')

# Commands
def start(q):
    if q == 'how_weather':
        say('天気は晴れです(適当)')
    elif q in ['what_day', 'what_date']:
        say('今日は' + date_text() + "です")
    elif q == 'is_sasago':
        say('今日は笹子の日' + ('です' if is_sasago_day() else 'ではないです' ))
    elif q == 'run_make_coffee':
        say('コーヒーはまだコントロールできません')
    elif q == 'absolute_duo':
        run_absolute()

def date_text():
    now = datetime.datetime.now()
    # NOTE: strftime は 0埋めされる
    day_str = '日,月,火,水,木,金,土'.split(',')[now.weekday()]
    return str(now.month) + '月' + str(now.day) + '日の' + day_str + '曜日'

def is_sasago_day():
    now = datetime.datetime.now()
    return now.day % 10 == 5

def fix_format_xml(text):
    return "".join(text.split("\n")[:-2])


if __name__ == '__main__':
    main()
