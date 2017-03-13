# -*- coding: utf-8 -*-
import os
import subprocess
import glob

home_path =  os.environ['HOME']
akane_path = os.path.join(home_path, 'akane-chan', 'main.py')

def shutup():
    killaudio_path = os.path.join(home_path, 'killaudio')
    subprocess.Popen(['sh', killaudio_path])

def say(message):
    shutup()
    print('echo >: ' +  message)
    # voice_process = subprocess.Popen([python3_path, akane_path] + message.split(), stdout=subprocess.PIPE)
    subprocess.Popen(['/usr/bin/python3', akane_path, message, "2.0", "1.4", "1.0", "1.0"])
    return 'message: ' + message

class Bot(object):
    def __init__(self):
        self._command = ''
        self._listeners = self._load_scripts()

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value

    def say(self, message):
        shutup()
        print('bot >: ' +  message)
        subprocess.Popen([python3_path, akane_path, message, "2.0", "1.4", "1.0", "1.0"])
    def listen(self, message):
        for listener in self._listeners:
            try:
                listener.main(self)
            except Exception as e:
                print(e)

    def _load_scripts():
        listeners = []
        for f in glob.glob('scripts/*.py'):
            moduleName = path.splitext(path.basename(f))[0]
            if (moduleName == '__init__'):
                continue
            module = importlib.import_module('scripts.' + moduleName)
            if callable(module.main):
                listeners.append(module)
        return listeners

    def stop_say(self):
        home_path = os.environ['HOME']
        killaudio_path = os.path.join(home_path, 'killaudio')
        subprocess.Popen(['sh', killaudio_path])
