say_coffee = '今日のコーヒーは'
f = open(coffee_now)
say_coffee = f.readlines()
f.close()
#say_coffee = 'オータムブレンド'
say('今日のコーヒーは' + say_coffee + 'す')
