# -*- coding: utf-8 -*-
import datetime

def is_sasago_day():
    now = datetime.datetime.now()
    return now.day % 10 == 5

def main(bot):
    if bot.command == 'is_sasago':
        bot.say('今日は笹子の日' + ('です' if is_sasago_day() else 'ではないです' ))
