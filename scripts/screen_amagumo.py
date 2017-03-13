# -*- coding: utf-8 -*-
import datetime
from cpschromecast import CpsChromecast
# TODO importの先を変更する

def screen_amagumo():
    say('雨雲をテレビに表示します')
    cc = CpsChromecast()
    cc.cast_rain_cloud()

def main(bot):
    if bot.command == 'screen_amagumo':
        screen_amagumo()
