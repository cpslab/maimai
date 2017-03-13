# -*- coding: utf-8 -*-
import os
import time
import subprocess

home_path =  os.environ['HOME']

# TODO pathを削除
unicorn_path = home_path + 'music/unicooooooon.wav'
tjm_path = home_path + 'maimai/play_tjm'
elzup_path = home_path + 'maimai/play_elzup'
shibomeu_path= home_path + 'maimai/play_shibomeu'
kyoshitsu_path = home_path + 'music/kyoshitsu.mp3'
miyano_path = home_path + 'music/miyano.mp3'
#  dear_kiss_path = home_path + 'music/dk.mp3'
#  transam_path = home_path + 'music/TRANS_AM.wav'

def main(bot):
    q = bot.command
    if q == 'unicorn':
        play_music(bot, unicorn_path)
    elif q == 'stretch':
        play_music(bot, miyano_path)
    elif q == 'play_tjm':
        play_tjm(bot)
    elif q == 'play_elzup':
        play_elzup(bot)
    elif q == 'play_shibomeu':
        play_shibomeu(bot)
#    elif q == 'dear_kiss':
#        play_music(dear_kiss_path)
#    elif q == 'transam':
#        play_music(transam_path)

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
