#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
from contextlib import closing
import commands
import xml.etree.ElementTree as ET
import datetime
import time
import random
import requests
import os

time.sleep(5)

# say
import subprocess
from flask import Flask
app = Flask(__name__)

home_path = '/home/pi/'
aques_path = home_path + 'speak_api/lib/aquestalkpi/AquesTalkPi'
akane_path = '/home/pi/akane-chan/main.py'

python3_path = '/usr/bin/python3'

killaudio_path = home_path + 'killaudio'

absolute_script_path = home_path + 'run_duo.py'
weather_cache_path = home_path + 'weather/today_weather_cache.txt'
weather_script_path = home_path + 'weather/get_weather.py'
unicorn_path = home_path + 'music/unicooooooon.wav'
transam_path = home_path + 'music/TRANS_AM.wav'

nas_path = '/mnt/nas/'
tjm_playlist_path = nas_path + 'iTunes Media/Music/Compilations/**/*.m4a'
elzup_playlist_path = nas_path + 'elzup/**/*.mp3'
shibomeu_playlist_path = nas_path + 'shibomeu/**/*'
tjm_path = home_path + 'maimai/play_tjm'
elzup_path = home_path + 'maimai/play_elzup'
shibomeu_path= home_path + 'maimai/play_shibomeu'


coffee_host = os.getenv('COFFEE_HOST')
print('coffee: ' + coffee_host)

food_list = ['かみなり', 'まつや', 'まつのや', 'あぶり', 'ささご', 'どんまる', 'てんや', 'カレー桜', 'イイトコ', 'ここのつ', 'かあちゃん', 'セブンイレブン', '学食', 'すた丼', 'おと', 'くらみそ', 'すき家', 'はなの舞', 'フードコート', '餃子太郎', 'つるかめ', 'らぼで自炊', 'いぶと']

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
    args = ['python', './cpschromecast.py']
    # args = ['mplayer', '-volume', '85', '-shuffle', tjm_playlist_path]
    subprocess.Popen(args)

def shutup():
    subprocess.Popen(['sh', killaudio_path])

def say(message):
    shutup()
    print('echo >: ' +  message)
    # voice_process = subprocess.Popen([python3_path, akane_path] + message.split(), stdout=subprocess.PIPE)
    subprocess.Popen([python3_path, akane_path, message, "2.0", "1.4", "1.0", "1.0"])
    return 'message: ' + message

def run_absolute():
    print('absolute')
    subprocess.Popen(['python2', absolute_script_path])

def run_weather():
    print('weather')
    p = subprocess.Popen(['cat', weather_cache_path], stdout=subprocess.PIPE)
    p.wait()
    stdout_data = p.stdout.read()
    say(stdout_data)

def main():
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    text_queue = ""
    separator = ".\n"
    is_state_recieve = False
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
        run_weather()
    elif q in ['what_day', 'what_date']:
        say('今日は' + date_text() + "です")
    elif q == 'is_sasago':
        say('今日は笹子の日' + ('です' if is_sasago_day() else 'ではないです' ))
    elif q == 'absolute_duo':
        run_absolute()
    elif q == 'random_food':
        say('今日のごはんは，' + random_food() + '，がおすすめ')
    elif q == 'coffee_run':
        try:
            say('おいしいコーヒーを入れますね')
            time.sleep(4)
            requests.get(coffee_host + '/coffee/0')
        except requests.exceptions.ConnectionError:
            say('働きたくないでござる')
    elif q == 'coffee_stop':
        try:
            requests.get(coffee_host + '/coffee/1')
            say('コーヒーをちゅうだんしました')
        except requests.exceptions.ConnectionError:
            say('働きたくないでござる')
    elif q == 'cancel':
        say('了解どすえー')
    elif q == 'goodnight':
        say('おやすみなさい，よいゆめを')
    elif q == 'hello':
        say('こんにちは')
    elif q == 'unicorn':
        play_music(unicorn_path)
#    elif q == 'transam':
#        play_music(transam_path)
    elif q == 'play_tjm':
        play_tjm()
    elif q == 'play_elzup':
        play_elzup()
    elif q == 'play_shibomeu':
        play_shibomeu()
    elif q == 'screen_amagumo':
        screen_amagumo()
    else:
        say(q + " というコマンドは覚えていないです")

def play_music(path):
    shutup()
    print(" ".join(['mplayer', '-volume', '100', path]))
    time.sleep(1)
    subprocess.Popen(['mplayer', '-volume', '100', path])

def random_food():
    return random.choice(food_list)

def date_text():
    now = datetime.datetime.now()
    # NOTE: strftime は 0埋めされる
    day_str = '月,火,水,木,金,土,日'.split(',')[now.weekday()]
    return str(now.month) + '月' + str(now.day) + '日の' + day_str + '曜日'

def is_sasago_day():
    now = datetime.datetime.now()
    return now.day % 10 == 5

def fix_format_xml(text):
    return "".join(text.split("\n")[:-2])


if __name__ == '__main__':
    main()
