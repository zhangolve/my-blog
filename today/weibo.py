from pathlib import Path
import bs4 as bs
from datetime import date


today = date.today()
d1 = today.strftime("-%m-%d")

def get_weibo_contents():
    working_dir = Path()
    contents = []
    for path in working_dir.glob("../weibo-backup/weibo/*.html"):
        with open(path.absolute()) as f:
            content = f.read()
            soup = bs.BeautifulSoup(content, 'html.parser')
            single_weibo_list = soup.findAll('div', {'class': 'WB_detail'})
            for single_weibo in single_weibo_list: 
                date = single_weibo.find(attrs={'node-type': 'feed_list_item_date'})
                if(date):
                    created_date = date.get('title')
                    if d1 in created_date:
                        contents.append(str(single_weibo))

    contents = '\n\n\n'.join(contents)
    if not contents:
        contents = 'there is no history blog'
    return contents
