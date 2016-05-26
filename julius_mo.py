# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import socket
from contextlib import closing
import commands
import xml.etree.ElementTree as ET

# say
import subprocess
from flask import Flask
app = Flask(__name__)

home_path = '/home/pi/'
aques_path = home_path + 'speak_api/lib/aquestalkpi/AquesTalkPi'


def say(message):
    voice_process = subprocess.Popen([aques_path] + message.split(), stdout=subprocess.PIPE)
    subprocess.Popen(['aplay'], stdin=voice_process.stdout)
    return 'message: ' + message


def main():
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    text_queue = ""
    separator = ".\n"

    while True:
        recv_data = sock.recv(bufsize)
        # print (recv_data)
        # parser.feed(recv_data)
        text_queue += recv_data
        if separator in text_queue:
            parts = text_queue.split(separator)
            xmls, text_queue = parts[:-1], parts[-1]
            print(xmls)
            for xml_text in xmls:
                try:
                    root = ET.fromstring(xml_text)
                    for word in root.iter('WHYPO'):
                        command = word.get('WORD')
                        start(command)
                    print(root)
                except ET.ParseError:
                    print('parce error--')
                    print(xml_text)
                    print('--')
    
def start(q):
    say(q)

def fix_format_xml(text):
    return "".join(text.split("\n")[:-2])


if __name__ == '__main__':
    main()
