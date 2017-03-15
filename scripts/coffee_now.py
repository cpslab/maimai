# -*- coding: utf-8 -*-
from util.hook import cmd

# TODO 相対path
coffee_now = '/home/pi/maimai/coffee_now'

@cmd("coffee_now")
def coffee_now(bot):
    f = open(coffee_now)
    say_coffee = f.readlines()[0]
    f.close()
    #say_coffee = 'オータムブレンド'
    bot.say('今日のコーヒーは「' + say_coffee + '」です')
