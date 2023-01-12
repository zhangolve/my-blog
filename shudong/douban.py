import leancloud
import feedparser
import os
from bs4 import BeautifulSoup
import datetime

# 解析豆瓣电影的rss feed文本
douban_rss = feedparser.parse('https://rsshub.app/douban/people/71828508/status')

leancloud.init("rkX7RdhzjQ0DdnpkcffRn4TD-gzGzoHsz", "pbWq8UDhvWbRpjebqfhqj4pG")



if os.environ.get('USER') == 'zhangolive':
    Shudong = leancloud.Object.extend('shudong_test')
else:
    Shudong = leancloud.Object.extend('shudong')

query = Shudong.query

DOUBAN_TYPE = 'douban'


def write_single_douban_shudong(text, published_at, photos=None):
    shudong = Shudong()
    shudong.set('content', text)
    shudong.set('type', DOUBAN_TYPE)
    shudong.set('published_at', published_at)
    if photos:
        shudong.set('photos', photos)
    shudong.save()

# 获取所有的电影信息
def get_all_douban_status():
    query.equal_to('type', DOUBAN_TYPE)
    query.exists('published_at')
    query.descending('published_at')
    result = query.find()
    for entry in douban_rss.entries:
        title = entry.title
        description = entry.description
        published = entry.published
        link = entry.link
        soup = BeautifulSoup(description, 'html.parser')
        text = title + soup.get_text()
        published_at = datetime.datetime.strptime(published, "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=datetime.timezone.utc)
        if not result:
            print('write', text)
            write_single_douban_shudong(text, published_at)
        else:
            last_published_at = result[0].get('published_at')
            if published_at > last_published_at:
                print('write:', text)
                write_single_douban_shudong(text, published_at)


get_all_douban_status()


