#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
from contextlib import closing
import commands
import xml.etree.ElementTree as ET
import datetime
import time
import requests
import os
import sys
sys.path.append("/home/pi")
from irkit import main as power_on
from cpschromecast import CpsChromecast

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
        pass

    def play_music(self, music_path):
        pass
        # 音楽を流す


home_path = '/home/pi/'
aques_path = home_path + 'speak_api/lib/aquestalkpi/AquesTalkPi'
akane_path = '/home/pi/akane-chan/main.py'

python3_path = '/usr/bin/python3'

killaudio_path = home_path + 'killaudio'

weather_cache_path = home_path + 'weather/today_weather_cache.txt'
weather_script_path = home_path + 'weather/get_weather.py'
unicorn_path = home_path + 'music/unicooooooon.wav'
kyoshitsu_path = home_path + 'music/kyoshitsu.mp3'
miyano_path = home_path + 'music/miyano.mp3'
dear_kiss_path = home_path + 'music/dk.mp3'
transam_path = home_path + 'music/TRANS_AM.wav'

nas_path = '/mnt/nas/'
tjm_playlist_path = nas_path + 'iTunes Media/Music/Compilations/**/*.m4a'
elzup_playlist_path = nas_path + 'elzup/**/*.mp3'
shibomeu_playlist_path = nas_path + 'shibomeu/**/*'
tjm_path = home_path + 'maimai/play_tjm'
elzup_path = home_path + 'maimai/play_elzup'
shibomeu_path= home_path + 'maimai/play_shibomeu'


coffee_host = os.getenv('COFFEE_HOST')
coffee_now = '/home/pi/maimai/coffee_now'
# print('coffee: ' + coffee_host)

def play_tjm():
    say('たじまさん，プレイリストスタート')
    time.sleep(3)
    args = ['sh', tjm_path]
    # args = ['mplayer', '-volume', '85', '-shuffle', tjm_playlist_path]
    subprocess.Popen(args)

def play_elzup():
    say('えるざっぷ，プレイリストスタート')
    time.sleep(3)
    args = ['sh', elzup_path]
    #  args = ['mplayer', '-volume', '85', '-shuffle', elzup_playlist_path]
    subprocess.Popen(args)

def play_shibomeu():
    say('しぼめう，プレイリストスタート')
    time.sleep(3)
    args = ['sh', shibomeu_path]
    # args = ['mplayer', '-volume', '85', '-shuffle', tjm_playlist_path]
    subprocess.Popen(args)

def screen_amagumo():
    say('雨雲をテレビに表示します')
    cc = CpsChromecast()
    cc.cast_rain_cloud()

def shutup():
    subprocess.Popen(['sh', killaudio_path])

def say(message):
    shutup()
    print('echo >: ' +  message)
    # subprocess.Popen([python3_path, aques_path, message])
    # voice_process = subprocess.Popen([python3_path, akane_path] + message.split(), stdout=subprocess.PIPE)
    subprocess.Popen([python3_path, akane_path, message, "2.0", "1.4", "1.0", "1.0"])
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
                start(command)
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

# Commands
def start(q):
    if q == 'how_weather':
        run_weather()
    elif q == 'coffee_run':
        try:
            say('おいしいコーヒーを入れますね')
            time.sleep(4)
            requests.get(coffee_host + '/coffee/0')
            time.sleep(5)
            play_music(kyoshitsu_path)
        except requests.exceptions.ConnectionError:
            say('働きたくないでござる')
    elif q == 'coffee_stop':
        try:
            requests.get(coffee_host + '/coffee/1')
            say('コーヒーをちゅうだんしました')
        except requests.exceptions.ConnectionError:
            say('働きたくないでござる')
    elif q == 'coffee_now':
        f = open(coffee_now)
        say_coffee = f.readlines()[0]
        f.close()
        #say_coffee = 'オータムブレンド'
        say('今日のコーヒーは「' + say_coffee + '」です')
    elif q == 'unicorn':
        play_music(unicorn_path)
#    elif q == 'dear_kiss':
#        play_music(dear_kiss_path)
#    elif q == 'transam':
#        play_music(transam_path)
    elif q == 'play_tjm':
        play_tjm()
    elif q == 'stretch':
        play_music(miyano_path)
    elif q == 'play_elzup':
        play_elzup()
    elif q == 'play_shibomeu':
        play_shibomeu()
    elif q == 'screen_amagumo':
        screen_amagumo()
    elif q == 'tv_on':
        say("テレビをつけます")
        power_on()
    # else:
        # say(q + " というコマンドは覚えていないです")

def play_music(path):
    shutup()
    print(" ".join(['mplayer', '-volume', '100', path]))
    time.sleep(1)
    subprocess.Popen(['mplayer', '-volume', '100', path])

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        bot.command = 'exit'
        for listener in listeners:
            try:
                listener.main(bot)
            except Exception as e:
                print(e)
        say('まいまい 停止します')
