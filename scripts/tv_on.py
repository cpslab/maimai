# -*- coding: utf-8 -*-
from util.hook import cmd
from irkit import main as power_on

timer_thread = None

@cmd('tv_on')
def tv_on(bot):
    bot.say("テレビをつけます")
    power_on()
