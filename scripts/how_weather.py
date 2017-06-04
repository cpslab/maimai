# -*- coding: utf-8 -*-
from util.hook import cmd
import os
import subprocess

home_path = '/home/pi'
weather_cache_path = os.path.join(home_path, 'weather', 'today_weather_cache.txt')

@cmd("how_weather")
def how_weather(bot):
    print('weather')
    p = subprocess.Popen(['cat', weather_cache_path], stdout=subprocess.PIPE)
    p.wait()
    stdout_data = p.stdout.read()
    bot.say(stdout_data)
