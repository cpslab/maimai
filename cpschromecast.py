# coding: UTF-8
import pychromecast
import urllib
from bs4 import BeautifulSoup


class CpsChromecast:
    def __init__(self):
        self.cast = pychromecast.get_chromecast(friendly_name="ChromecastCPS")
        self.cast.wait()
        self.mc = self.cast.media_controller

    def play_media(self, url, content_type):
        self.mc.play_media(url, content_type)

    def play_image(self, url):
        # TODO: png jpg でも何故か行ける
        self.play_media(url, 'image/gif')

    def play_mp4(self, url):
        self.play_media(url, 'video/mp4')

    def cast_rain_cloud(self):
        self.play_image(self.scrape_raincloud_image_url())

    def scrape_raincloud_image_url(self):
        html = urllib.urlopen('http://weather.yahoo.co.jp/weather/raincloud/')
        soup = BeautifulSoup(html, 'lxml')
        return soup.find('td', class_='mainImg').find('img')['src']
