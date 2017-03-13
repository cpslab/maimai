# -*- coding: utf-8 -*-
import os
import subprocess

home_path =  os.environ['HOME']
absolute_script_path = os.path.join(home_path, 'run_duo.py')

def run_absolute():
    # TODO 直接import
    subprocess.Popen(['python2', absolute_script_path])

def main(bot):
    if bot.command == 'absolute_duo':
        run_absolute()
