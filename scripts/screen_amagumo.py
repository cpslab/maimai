# -*- coding: utf-8 -*-
from util.hook import cmd
import datetime
from cpschromecast import CpsChromecast
# TODO importの先を変更する

@cmd('screen_amagumo')
def screen_amagumo(bot):
    bot.say('雨雲をテレビに表示します')
    cc = CpsChromecast()
    cc.cast_rain_cloud()
