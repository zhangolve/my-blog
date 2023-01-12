# https://rsshub.app/douban/people/62759792/status

import feedparser

# 解析豆瓣电影的rss feed文本
douban_rss = feedparser.parse('https://rsshub.app/douban/people/71828508/status')

# 获取所有的电影信息
for entry in douban_rss.entries:
    print(entry)
    title = entry.title

    description = entry.description

    
    published = entry.published

    link = entry.link

    print(title, description, link, published)


# If some 设置树洞类型，type=douban . 自定义pubdate ..比较pubdate，大于上一个pubdate的才存起来。
