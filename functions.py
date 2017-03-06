# -*- coding: utf-8 -*-
import subprocess
import requests
import maimai.funcpath
import time
import random
import datetime

from maimai.cpschromecast import CpsChromecast

p = maimai.funcpath.Funcpath()

def play_music_list(message, path):
    """pathに指定した再生リストを起動してmessageを読み上げる"""
    say(message + '，プレイリストスタート')
    time.sleep(3)  # 喋っている間待つ
    args = ['sh', path]
    subprocess.Popen(args)


def screen_amagumo():
    """chromecastを起動してテレビに現在の雨雲の状態を標示する"""
    say('雨雲をテレビに表示します')
    cc = CpsChromecast()
    cc.cast_rain_cloud()


def shutup():
    """再生中の音をすべて止める"""
    subprocess.Popen(['sh', p.killaudio_path])


def say(message):
    """再生中の音をすべて止めて指定したメッセージを読み上げる"""
    shutup()
    print('echo >: ' +  message)
    subprocess.Popen([p.python3_path, p.akane_path, message, "2.0", "1.4", "1.0", "1.0"])  # オプションの数字はvolume,speed,pitch.rangeの順番
    return 'message: ' + message


def run_absolute():
    """スピーカー再起動用のスクリプトを走らせる"""
    print('absolute')
    subprocess.Popen(['python2', p.absolute_script_path])


def run_weather():
    """今日の天気を取得して喋らせる"""
    print('weather')
    p = subprocess.Popen(['cat', p.weather_cache_path], stdout=subprocess.PIPE)
    p.wait()
    stdout_data = p.stdout.read()
    say(stdout_data)


def run_coffee(bool):
    """Trueでコーヒーを淹れるFalseでコーヒーメーカーをストップ"""
    if bool:
        try:
            say('おいしいコーヒーを入れますね')
            time.sleep(4)
            requests.get(p.coffee_host + '/coffee/0')
            time.sleep(5)
            play_music(p.kyoshitsu_path)
        except requests.exceptions.ConnectionError:
            say('働きたくないでござる')
    else:
        try:
            requests.get(p.coffee_host + '/coffee/1')
            say('コーヒーをちゅうだんしました')
        except requests.exceptions.ConnectionError:
            say('働きたくないでござる')

def now_coffee():
    """コーヒーメーカーに入ってるコーヒーの銘柄を返す"""
    f = open(p.coffee_now)
    say_coffee = f.readlines()[0]
    f.close()
    say('今日のコーヒーは「' + say_coffee + '」です')


def play_music(path):
    """pathにある音楽ファイルを再生する"""
    shutup()
    print(" ".join(['mplayer', '-volume', '100', path]))
    time.sleep(1)
    subprocess.Popen(['mplayer', '-volume', '100', path])


def random_food():
    """飲食店の名前をランダムに返す"""
    f = open(p.food_list)
    food_list = f.readlines()
    food_list = [i[:-1] for i in food_list]
    f.close()
    return random.choice(food_list)


def date_text():
    """今日の日付を返す"""
    now = datetime.datetime.now()
    # NOTE: strftime は 0埋めされる
    day_str = '月,火,水,木,金,土,日'.split(',')[now.weekday()]
    return str(now.month) + '月' + str(now.day) + '日の' + day_str + '曜日'


def is_sasago_day():
    """今日が笹互の日かどうかを返す"""
    now = datetime.datetime.now()
    return now.day % 10 == 5