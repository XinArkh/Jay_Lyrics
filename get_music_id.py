# coding:utf-8

from bs4 import BeautifulSoup

f = open("music_id_origin.txt", "r")
content = f.read()
f.close()

def get_id():
    idList = []
    bsObj = BeautifulSoup(content)
    dataList = bsObj.findAll("span", {"data-res-action":"mv"})
    for data in dataList:
        idList.append(data.attrs["data-res-id"])
        # print(data.attrs["data-res-id"])
    return idList

# ids = get_id()
# print(ids[2])

# for id in ids:
#     print(id)