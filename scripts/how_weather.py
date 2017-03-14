# -*- coding: utf-8 -*-
import os
import subprocess

home_path =  os.environ['HOME']
weather_cache_path = os.path.join(home_path, 'weather', 'today_weather_cache.txt')

def main(bot):
    if bot.command == 'how_weather':
        print('weather')
        p = subprocess.Popen(['cat', weather_cache_path], stdout=subprocess.PIPE)
        p.wait()
        stdout_data = p.stdout.read()
        bot.say(stdout_data)

