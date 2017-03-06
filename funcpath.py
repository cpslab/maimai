# -*- coding: utf-8 -*-
import os


class FuncPath(object):
    """各機能を動かすスクリプトやファイルが置いてあるパス"""
    def __init__(self):
        self._home_path = '/home/pi/'

        # 喋るコマンド系
        self._aques_path = self._home_path + 'speak_api/lib/aquestalkpi/AquesTalkPi'
        self._akane_path = '/home/pi/akane-chan/main.py'
        self._killaudio_path = self._home_path + 'killaudio'
        self._python3_path = '/usr/bin/python3'

        # スピーカー再起動用
        self._absolute_script_path = self._home_path + 'run_duo.py'

        # お天気標示用
        self._weather_cache_path = self._home_path + 'weather/today_weather_cache.txt'
        self._weather_script_path = self._home_path + 'weather/get_weather.py'

        # nasにアクセスして音楽を鳴らす機能用
        self._nas_path = '/mnt/nas/'
        self._tjm_playlist_path = self._nas_path + 'iTunes Media/Music/Compilations/**/*.m4a'
        self._elzup_playlist_path = self._nas_path + 'elzup/**/*.mp3'
        self._shibomeu_playlist_path = self._nas_path + 'shibomeu/**/*'
        self._tjm_path = self._home_path + 'maimai/play_tjm'
        self._elzup_path = self._home_path + 'maimai/play_elzup'
        self._shibomeu_path= self._home_path + 'maimai/play_shibomeu'

        # コーヒーサーバ用
        self._coffee_host = os.getenv('COFFEE_HOST')
        self._coffee_now = '/home/pi/maimai/coffee_now'

        #  FoodList用
        self._food_list = self._home_path + 'maimai/foodlist'

        # その他の音楽を鳴らすだけの機能用
        self._unicorn_path = self._home_path + 'music/unicooooooon.wav'
        self._kyoshitsu_path = self._home_path + 'music/kyoshitsu.mp3'
        self._miyano_path = self._home_path + 'music/miyano.mp3'
        self._dear_kiss_path = self._home_path + 'music/dk.mp3'
        self._transam_path = self._home_path + 'music/TRANS_AM.wav'

    def get_home_path(self):
        return self._home_path
    home_path = property(get_home_path)

    def get_aques_path(self):
        return self._aques_path
    aques_path = property(get_aques_path)

    def get_akane_path(self):
        return self._akane_path
    akane_path = property(get_akane_path)

    def get_killaudio_path (self):
        return self._killaudio_path
    killaudio_path = property(get_killaudio_path)

    def get_python3_path (self):
        return self._python3_path
    python3_path = property(get_python3_path)

    def get_absolute_script_path (self):
        return self._absolute_script_path
    absolute_script_path  = property(get_absolute_script_path)

    def get_weather_cache_path (self):
        return self._weather_cache_path
    weather_cache_path = property(get_weather_cache_path)

    def get_weather_script_path (self):
        return self._weather_script_path
    weather_script_path = property(get_weather_script_path)

    def get_tjm_playlist_path (self):
        return self._tjm_playlist_path
    tjm_playlist_path = property(get_tjm_playlist_path)

    def get_elzup_playlist_path (self):
        return self._elzup_playlist_path
    elzup_playlist_path = property(get_elzup_playlist_path)

    def get_shibomeu_playlist_path (self):
        return self._shibomeu_playlist_path
    shibomeu_playlist_path = property(get_shibomeu_playlist_path)

    def get_tjm_path (self):
        return self._tjm_path
    tjm_path = property(get_tjm_path)

    def get_elzup_path (self):
        return self._elzup_path
    elzup_path = property(get_elzup_path)

    def get_shibomeu_path (self):
        return self._shibomeu_path
    shibomeu_path = property(get_shibomeu_path)

    def get_coffee_host(self):
        return self._coffee_host
    coffee_host = property(get_coffee_host)

    def get_coffee_now(self):
        return self._coffee_now
    coffee_now = property(get_coffee_now)

    def get_unicorn_path (self):
        return self._unicorn_path
    unicorn_path = property(get_unicorn_path)

    def get_kyoshitsu_path (self):
        return self._kyoshitsu_path
    kyoshitsu_path = property(get_kyoshitsu_path)

    def get_miyano_path (self):
        return self._miyano_path
    miyano_path = property(get_miyano_path)

    def get_dear_kiss_path (self):
        return self._dear_kiss_path
    dear_kiss_path = property(get_dear_kiss_path)

    def get_transam_path (self):
        return self._transam_path
    transam_path = property(get_transam_path)

    def get_food_list (self):
        return self._food_list
    food_list = property(get_food_list)