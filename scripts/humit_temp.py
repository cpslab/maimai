# -*- coding: utf-8 -*-
from util.hook import cmd
import urllib2

def fetchAPI():
    res = urllib2.urlopen('http://192.168.1.172')
    return res.read().split(url)

@cmd("now_humid")
def now_humid(bot):
    t, h = fetchAPI()
    bot.say(h + "パーセントです")

@cmd("now_temp")
def now_temp(bot):
    t, h = fetchAPI()
    bot.say(t + "どです")
