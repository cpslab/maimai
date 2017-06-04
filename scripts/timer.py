# -*- coding: utf-8 -*-
from util.hook import cmd
import threading

timer_thread = None

@cmd('timer_5m')
def timer_5m(bot):
    bot.say('5ふんタイマーをセットしました')
    timer_thread = threading.Timer(5 * 60, lambda: bot.say('5ふんたちましたよ'))
    timer_thread.start()

@cmd('timer_30m')
def timer_30m(bot):
    bot.say('30ふんタイマーをセットしました')
    timer_thread = threading.Timer(30 * 60, lambda: bot.say('30ふんたちましたよ'))
    timer_thread.start()

@cmd('exit')
def timr_exit(bot):
    if timer_thread and timer_thread.isAlive():
        timer_thread.cancel()
