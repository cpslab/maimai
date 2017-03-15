# -*- coding: utf-8 -*-
from util.hook import cmd

@cmd("goodnight")
def goodnight(bot):
    bot.say('おやすみなさい，よいゆめを')

@cmd("hello")
def hello(bot):
    bot.say('こんにちは')
