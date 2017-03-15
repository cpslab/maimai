# -*- coding: utf-8 -*-
from util.hook import cmd

@cmd("exit")
def main(bot):
    bot.say('まいまい 停止します')
