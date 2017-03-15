# -*- coding: utf-8 -*-
from util.hook import cmd
import datetime

def is_sasago_day():
    now = datetime.datetime.now()
    return now.day % 10 == 5

@cmd("is_sasago")
def main(bot):
    bot.say('今日は笹子の日' + ('です' if is_sasago_day() else 'ではないです' ))
