from pathlib import Path
from datetime import datetime
from mail_sender import MailSender
from weibo import get_weibo_contents

import pytz

# 获取当前时间（使用本地时间）
local_tz = pytz.timezone('Asia/Shanghai')
today = datetime.now(local_tz)

# 获取日期部分并格式化
d1 = today.strftime("-%m-%d")

my_sender = '1993oliver.zhang@gmail.com'
my_pass = 'tfwrnhhtacfgpdvo'

receiver_addr = ['zhangolve@gmail.com']
sender_name = 'History blog'
subject = 'history blog ' + today.strftime("%Y-%m-%d %H:%M:%S")



working_dir = Path()
contents = []
for path in working_dir.glob("../**/*.md"):
    # include md file / weibo / txt csv ... files 
    # sort by date
    # html to markdown
    md_blogs = []
    txt_blogs = []
    weibo = []
    with open(path.absolute(), encoding="utf-8") as f:
        content = f.read()
        if d1 in content:            
            contents.append(content)
contents = '\n\n\n'.join(contents)
html= get_weibo_contents()

if not contents:
    contents = 'there is no history blog'

mailsender=MailSender(my_sender, my_pass, sender_name, receiver_addr, subject, contents, html, None)
mailsender.send_it()
