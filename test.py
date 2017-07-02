from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def get_lyrics(id):
    html = urlopen("http://music.163.com/api/song/lyric?os=pc&id=" + str(id) + "&lv=-1&kv=-1&tv=-1")
    bsObj = BeautifulSoup(html)
    lyric_origin = bsObj.p.get_text()
    lyric = json.loads(lyric_origin)
    lyric = lyric['lrc']['lyric']
    print(lyric)

get_lyrics(185910)