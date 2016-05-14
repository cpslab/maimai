辞書追加:
iconv -f utf8 -t eucjp ./weather.yomi | ~/julius-kits/dictation-kit-v4.3.1-linux/bin/yomi2voca.pl > ~/julius-kits/dictation-kit-v4.3.1-linux/weather.dic


Julius起動:
pi@raspberrypi ~/microphone_dict $ ALSADEV="plughw:2,0" ~/julius-4.3.1/julius/julius -C ~/julius-kits/dictation-kit-v4.3.1-linux/weather.jconf -nostrip

Julius サーバー起動:
pi@raspberrypi ~/microphone_dict $ ALSADEV="plughw:2,0" ~/julius-4.3.1/julius/julius -C ~/julius-kits/dictation-kit-v4.3.1-linux/weather.jconf -nostrip -module
