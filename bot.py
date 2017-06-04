# -*- coding: utf-8 -*-
import os
import subprocess
import glob
import sys
import importlib

home_path = '/home/pi'
akane_path = os.path.join(home_path, 'akane-chan', 'main.py')
aques_path = os.path.join(home_path, 'speak_api/lib/aquestalkpi/AquesTalkPi')

class Bot(object):
    def __init__(self):
        self._cmd = ''
        self._listeners = self._load_scripts()

    @property
    def cmd(self):
        return self._cmd

    @property
    def listeners(self):
        return self._listeners

    @cmd.setter
    def cmd(self, value):
        self._cmd = value

    def say(self, message):
        self.stop_say()
        print('bot >: ' +  message)
        voice_process = subprocess.Popen([aques_path] + message.split(), stdout=subprocess.PIPE)
        subprocess.Popen(['aplay'], stdin=voice_process.stdout)
        # subprocess.Popen([python3_path, akane_path, message, "2.0", "1.4", "1.0", "1.0"])

    def listen(self, cmd):
        self.cmd = cmd  
        for l in self.listeners:
            if hasattr(l, "_command"):
                try:
                    if l._command == self.cmd:
                        l(self)
                    else:
                        l(self)
                except Exception as e:
                    print(e)

    def _load_scripts(self):
        sys.path += ['scripts']
        listeners = []
        for f in glob.glob('scripts/*.py'):
            module_name = os.path.splitext(os.path.basename(f))[0]
            module = importlib.import_module('scripts.' + module_name)
            for x in dir(module):
                method = getattr(module, x)
                if hasattr(method, "_hook"):
                    listeners.append(getattr(module, x))
        return listeners

    def stop_say(self):
        killaudio_path = os.path.join(home_path, 'killaudio')
        subprocess.Popen(['sh', killaudio_path])
