# -*- coding: utf-8 -*-
import urllib2

def fetchAPI():
    res = urllib2.urlopen('http://192.168.1.172')
    return res.read().split(url)

def main(bot):
    if bot.command == 'now_humid':
        t, h = fetchAPI()
        bot.say(h + "パーセントです")
    elif bot.command == 'now_temp':
        t, h = fetchAPI()
        bot.say(t + "どです")
