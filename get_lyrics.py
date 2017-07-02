# coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

def clean_lyric(lyric_origin):
    lyric = json.loads(lyric_origin)
    lyric = lyric['lrc']['lyric']
    lyric = re.sub('\[........*\]', '', lyric)
    lyric = re.sub(' +', ' ', lyric)

    lyric = re.sub("\xa0|\uc65c|\uc65c|\ub0b4|\ub6f0|\uc5d0|\ub530|\ub77c|\uc624|\ub294|\uac1c|\ub4e4|\uc774|\uc788|\ub098|\uc77c", ' ', lyric)
    lyric = re.sub("\ubd80|\ub7ec|\ub0a8|\uc758|\uc778|\uc0dd|\uc0ac|\uace0|\ud30c|\uce58|\uc544|\ub09c|\ud544|\uc694|\uc5c6|\ub2e4", ' ', lyric)
    lyric = re.sub("\ub178|\ub798|\ub05d|\uae30|\uc804|\uac00|\ubcd1|\uc6d0|\ubcf4|\uc904|\uae4c|\ub9d0|\uc810|\uc9c0|\ud504|\ubc84", ' ', lyric)
    lyric = re.sub("\uc2dc|\ub85c|\ud130|\ud53c|\ud574|\ubc1b|\uc740|\ud328|\ubc00|\ub9ac|\uc81c|\uba48|\ucdb0|\uadf8|\ub9cc|\ud558", ' ', lyric)
    lyric = re.sub("\uaebc|\uc838|\ub824|\uc918|\ub2c8|\ub9d8|\ub300|\uc0b4|\uc2f6|\uc5b4|\u015f|\u0131", ' ', lyric)
    ##########上面这些代码无法用GBK编码写入文本文件，只好手动一次一次运行，看着报错信息添加到替换选项中，##########
    ##########最后发现是卡在《四面楚歌》中，这首歌的歌词中有一部分是韩文，所以应该是无法写入韩文引起的问题##########

    return lyric

def download_lyric(id, lyric):
    address = "lyrics\\" + str(id) + ".txt"
    f = open(address, 'w')
    f.write(lyric)
    f.close()

def get_lyrics(id):
    html = urlopen("http://music.163.com/api/song/lyric?os=pc&id=" + str(id) + "&lv=-1&kv=-1&tv=-1")
    bsObj = BeautifulSoup(html)
    lyric_origin = bsObj.p.get_text()
    lyric = clean_lyric(lyric_origin)
    download_lyric(id, lyric)

#     lyric = json.loads(lyric_origin)['lrc']['lyric']
#     print(lyric)
#
# get_lyrics(185910)