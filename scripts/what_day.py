# -*- coding: utf-8 -*-
import datetime

def date_text():
    now = datetime.datetime.now()
    # NOTE: strftime は 0埋めされる
    day_str = '月,火,水,木,金,土,日'.split(',')[now.weekday()]
    return str(now.month) + '月' + str(now.day) + '日の' + day_str + '曜日'

def main(bot):
    if bot.command == in ['what_day', 'what_date']:
        bot.say('今日は' + date_text() + "です")
