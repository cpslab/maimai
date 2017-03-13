# -*- coding: utf-8 -*-
from irkit import main as power_on

timer_thread = None

def main(bot):
    if bot.command == 'tv_on':
        bot.say("テレビをつけます")
        power_on()
