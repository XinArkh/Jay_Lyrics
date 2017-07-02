# coding:utf-8

from jay_practice import get_music_id
from jay_practice import get_lyrics
import os
import jieba
from collections import Counter

##########下载歌词到本地，如本地已有歌词可注释掉此段代码，提高运行效率##########
# idList = get_music_id.get_id()
# for id in idList:
#     get_lyrics.get_lyrics(id)
################################################################################

words = []
for file in os.listdir('lyrics'):
    with open('lyrics\\' + file) as f:
        lyric = f.read()
        word_piece = jieba.cut(lyric)
        words.extend(set(word_piece))  # 记录词句出现的次数，一首歌出现多次按一次计，如果改成words.extend(word_piece)，一首歌出现多次将按多次计

count = Counter(words)
result = sorted(count.items(), key = lambda  x:x[1], reverse = True)
f = open("result.txt", 'w')
f.write("词句\t出现次数")
for res in result:
    # print(res[0], res[1])
    res_piece = res[0] + "\t" + str(res[1]) + "\n"
    f.write(res_piece)

f.close()