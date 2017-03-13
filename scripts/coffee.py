# -*- coding: utf-8 -*-
import time
import requests

# TODO 相対path
kyoshitsu_path = home_path + 'music/kyoshitsu.mp3'

# TODO not exist
coffee_host = os.getenv('COFFEE_HOST')

def main(bot):
    if bot.command == 'coffee_run':
        try:
            robot.say('おいしいコーヒーを入れますね')
            time.sleep(4)
            requests.get(coffee_host + '/coffee/0')
            time.sleep(5)
            play_music(kyoshitsu_path)
        except requests.exceptions.ConnectionError:
            robot.say('働きたくないでござる')
    elif q == 'coffee_stop':
        try:
            requests.get(coffee_host + '/coffee/1')
            robot.say('コーヒーをちゅうだんしました')
        except requests.exceptions.ConnectionError:
            robot.say('働きたくないでござる')

def play_music(bot, path):
    bot.stop_say()
    print(" ".join(['mplayer', '-volume', '100', path]))
    time.sleep(1)
    subprocess.Popen(['mplayer', '-volume', '100', path])
