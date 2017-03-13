# -*- coding: utf-8 -*-
import threading

timer_thread = None

def main(bot):
    if bot.command == 'timer_5m':
        bot.say('5ふんタイマーをセットしました')
        timer_thread = threading.Timer(5 * 60, lambda: bot.say('5ふんたちましたよ'))
        timer_thread.start()
    elif bot.command == 'timer_30m':
        bot.say('30ふんタイマーをセットしました')
        timer_thread = threading.Timer(30 * 60, lambda: bot.say('30ふんたちましたよ'))
        timer_thread.start()
    elif bot.command == 'exit':
        if timer_thread and timer_thread.isAlive():
            timer_thread.cancel()
