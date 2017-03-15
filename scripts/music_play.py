# -*- coding: utf-8 -*-
from util.hook import cmd
import os
import time
import subprocess

home_path =  os.environ['HOME']

@cmd("unicorn")
def unicorn(bot):
    unicorn_path = home_path + 'music/unicooooooon.wav'
    play_music(bot, unicorn_path)

@cmd("stretch")
def stretch(bot):
    miyano_path = home_path + 'music/miyano.mp3'
    play_music(bot, miyano_path)

@cmd("play_tjm")
def play_tjm(bot):
    tjm_path = home_path + 'maimai/play_tjm'
    play_tjm(bot)

@cmd("play_elzup")
def play_elzup(bot):
    elzup_path = home_path + 'maimai/play_elzup'
    play_elzup(bot)

@cmd("play_shibomeu")
def play_shibomeu(bot):
    shibomeu_path= home_path + 'maimai/play_shibomeu'
    play_shibomeu(bot)

def play_music(bot, path):
    bot.stop_say()
    args = ['mplayer', '-volume', '100', path]
    print(" ".join(args))
    time.sleep(1)
    subprocess.Popen(args)

def play_user(bot, message, user_path):
    bot.say(message)
    time.sleep(3)
    subprocess.Popen(['sh', user_path])

def play_tjm(bot):
    # args = ['mplayer', '-volume', '85', '-shuffle', tjm_playlist_path]
    play_user(bot, 'たじまさん，プレイリストスタート', tjm_path)

def play_elzup(bot):
    #  args = ['mplayer', '-volume', '85', '-shuffle', elzup_playlist_path]
    play_user(bot, 'えるざっぷ，プレイリストスタート', elzup_path)

def play_shibomeu(bot):
    # args = ['mplayer', '-volume', '85', '-shuffle', tjm_playlist_path]
    play_user(bot, 'しぼめう，プレイリストスタート', shibomeu_path)

def play_music(bot, path):
    bot.stop_say()
    print(" ".join(['mplayer', '-volume', '100', path]))
    time.sleep(1)
    subprocess.Popen(['mplayer', '-volume', '100', path])
