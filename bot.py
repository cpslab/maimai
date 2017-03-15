# -*- coding: utf-8 -*-
import os
import subprocess
import glob
import sys
import importlib

home_path =  os.environ['HOME']
akane_path = os.path.join(home_path, 'akane-chan', 'main.py')

class Bot(object):
    def __init__(self):
        self._cmd = ''
        self._listeners = self._load_scripts()

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        self._cmd = value

    def say(self, message):
        self.stop_say()
        print('bot >: ' +  message)
        subprocess.Popen([python3_path, akane_path, message, "2.0", "1.4", "1.0", "1.0"])

    def listen(self, cmd):
        self.cmd = cmd  
        for l in self._listeners:
            if hasattr(l, "_command"):
                try:
                    if l._command == self.cmd:
                        l(self)
                    else:
                        l(self)
                except Exception as e:
                    print(e)

    def _load_scripts():
        sys.path += ['scripts']
        for f in glob('scripts/*.py'):
            module_name = path.splitext(path.basename(f))[0]
            module = importlib.import_module('scripts.' + module_name)
            for x in dir(module):
                method = getattr(module, x)
                if hasattr(method, "_hook"):
                    bot.add_listener(getattr(module, x))

    def add_listener(self, listener):
        self._listeners.append(listener)

    def stop_say(self):
        home_path = os.environ['HOME']
        killaudio_path = os.path.join(home_path, 'killaudio')
        subprocess.Popen(['sh', killaudio_path])
