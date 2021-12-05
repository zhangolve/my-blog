from pathlib import Path
from datetime import date
from mail_sender import MailSender
from weibo import get_weibo_contents

today = date.today()
d1 = today.strftime("-%m-%d")

my_sender = '1262010981@qq.com'
my_pass = 'nrrejsviolzpjchd'
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
