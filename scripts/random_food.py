# -*- coding: utf-8 -*-
from util.hook import cmd
import random

food_list = [
    'かみなり',
    'まつや',
    'まつのや',
    'あぶり',
    'ささご',
    'どんまる',
    'てんや',
    'カレー桜',
    'イイトコ',
    'ここのつ',
    'かあちゃん',
    'セブンイレブン',
    '学食',
    'すた丼',
    'おと',
    'くらみそ',
    'すき家',
    'はなの舞',
    'フードコート',
    '餃子太郎',
    'つるかめ',
    'らぼで自炊',
    'いぶと',
    'ぽぽらまーま',
    'しんぱち食堂'
]

@cmd('random_food')
def random_food(bot):
    bot.say('今日のごはんは，' + random.choice(food_list) + '，がおすすめ')
