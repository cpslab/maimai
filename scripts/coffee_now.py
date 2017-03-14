# -*- coding: utf-8 -*-
# TODO 相対path
coffee_now = '/home/pi/maimai/coffee_now'

def main(bot):
    if bot.command == 'coffee_now':
        f = open(coffee_now)
        say_coffee = f.readlines()[0]
        f.close()
        #say_coffee = 'オータムブレンド'
        bot.say('今日のコーヒーは「' + say_coffee + '」です')
