#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
import xml.etree.ElementTree as ET
import sys
import maimai.funcpath
import maimai.functions as func
sys.path.append("/home/pi")
from irkit import main as power_on

p = maimai.funcpath.FuncPath()


def main():
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    text_queue = ""
    separator = ".\n"
    is_state_recieve = False
    func.say('まいまい起動しました')

    while True:
        recv_data = sock.recv(bufsize)
        text_queue += recv_data
        if separator in text_queue:
            parts = text_queue.split(separator)
            xmls, text_queue = parts[:-1], parts[-1]
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
                            func.shutup()
                        elif command == 'start':
                            if cm <= 0.94:
                                continue
                            is_state_recieve = True
                            func.say('はい')
                            break
                        elif is_state_recieve:
                            if cm < 0.94:
                                func.say('え？')
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
        func.run_weather()
    elif q in ['what_day', 'what_date']:
        func.say('今日は' + func.date_text() + "です")
    elif q == 'is_sasago':
        func.say('今日は笹子の日' + ('です' if func.is_sasago_day() else 'ではないです' ))
    elif q == 'absolute_duo':
        func.run_absolute()
    elif q == 'random_food':
        func.say('今日のごはんは，' + func.random_food() + '，がおすすめ')
    elif q == 'coffee_run':
        func.run_coffee(True)
    elif q == 'coffee_stop':
        func.run_coffee(False)
    elif q == 'coffee_now':
        func.now_coffee()
    elif q == 'cancel':
        func.say('了解どすえー')
    elif q == 'goodnight':
        func.say('おやすみなさい，よいゆめを')
    elif q == 'hello':
        func.say('こんにちは')
    elif q == 'unicorn':
        func.play_music(p.unicorn_path)
    elif q == 'stretch':
        func.play_music(p.miyano_path)
    elif q == 'play_tjm':
        func.play_music_list('たじまさん', p.tjm_path)
    elif q == 'play_elzup':
        func.play_music_list('えるざっぷ', p.elzup_path)
    elif q == 'play_shibomeu':
        func.play_music_list('しぼめう', p.shibomeu_path)
    elif q == 'screen_amagumo':
        func.screen_amagumo()
    elif q == 'tv_on':
        func.say("テレビをつけます")
        power_on()
    else:
        func.say(q + " というコマンドは覚えていないです")


if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        func.say('まいまい 停止します')
