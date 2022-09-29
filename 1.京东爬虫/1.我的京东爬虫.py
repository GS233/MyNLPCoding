import requests
import csv
import re
import time
from lxml import etree
from lxml import html
import random
''' https://club.jd.com/comment/productPageComments.action '''
'''
    callback: fetchJSON_comment98
    productId: 100027789707
    score: 0
    sortType: 5
    page: 0
    pageSize: 10
    isShadowSku: 0
    fold: 1
'''
comment_url = 'https://club.jd.com/comment/productPageComments.action'

f = open("101.JDcomments.csv", mode="a", encoding="utf-8", newline='')
csvwriter = csv.writer(f)
'''
row = ('评论', '评分')
csvwriter.writerow(row)
'''

headers = {
    'cookie':'token=45d768418a50901a8f72e3bf5026320c,2,923820; Expires=Sun, 11 Sep 2022 06:30:00 GMT; Max-Age=1800; Domain=.jd.com; Path=/',
    'referer': 'https://item.jd.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

obj = re.compile(r'{(?P<comments>.*?)},', re.S)
objCommet = re.compile(r',"guid":".*?".*?,"content":"(?P<comment>.*?)",', re.S)
# "score":2,"
objScore = re.compile(r'"score":(?P<score>.*?),"', re.S)
index = 0
for i in range(100):
    page = i
    print("Page:",page)
    '''
    params = { # 中差评
        'productId': 100015330230,  # 商品id,先写死
        'score': 2,
        'sortType': 6,
        'page': page,
        'pageSize': 10,
        'callback': 'fetchJSON_comment98',
        'isShadowSku': 0,
        'fold': 1
    }

    '''
    params = { # 全评
        'productId': 100015330230,  # 商品id,先写死
        'score': 0,
        'sortType': 5,
        'page': page,
        'pageSize': 10,
        'callback': 'fetchJSON_comment98',
        'isShadowSku': 0,
        'fold': 1
    }
       

    comment_resp = requests.get(url=comment_url,params=params,headers=headers)
    comment_resp.close()
    text = comment_resp.text

    Jsons = obj.finditer(text)
    for it in Jsons:
        page_comment = []
        page_score = []
        json = it.group("comments")
        comments = objCommet.finditer(json)
        scores = objScore.finditer(json)
        for comment,score in zip(comments,scores):
            comment = comment.group("comment")
            score = score.group("score")
            print(comment) 
            print(score)   
            csvwriter.writerow([comment,score])

    time.sleep(5)

print("over!")
 


