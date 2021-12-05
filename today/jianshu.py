import requests
import json
from datetime import datetime
import os
from markdownify import markdownify

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

# https://www.jianshu.com/author/notebooks


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'cookie': 'web_login_version=MTYzODE1MjUxMA%3D%3D--23f304ec938735ec2dad5ccd8f240d33d9a7b81f; remember_user_token=W1s0ODE4MF0sIiQyYSQxMCRvbWFmQkgyUzh5bHU3M1hwZWNmLi9lIiwiMTYzODY3MDkxMi45MDkyMTU1Il0%3D--d7a4f122698da1c7dc67af7023e9240a0487e14d; read_mode=day; default_font=font2; locale=zh-CN; _m7e_session_core=660513a5223504887c44b62d4ae4e923; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d697f72e783b-092828bc4a1ae1-978183a-2073600-17d697f72e8d04%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d697f72e783b-092828bc4a1ae1-978183a-2073600-17d697f72e8d04%22%7D'
}

notebooks_res = requests.get('https://www.jianshu.com/author/notebooks', headers=headers)   

notebooks = json.loads(notebooks_res.text)

new_notebooks = notebooks[-7]
print(new_notebooks)
for notebook in [new_notebooks]:
    notes_res = requests.get('https://www.jianshu.com/author/notebooks/'+str(notebook.get('id'))+'/notes', headers=headers)     
    notes = json.loads(notes_res.text)
    notebook_name = notebook.get('name')
    os.makedirs(notebook.get('name'))
    for note in notes:
        title = note.get('title')
        date_timestamp = note.get('content_updated_at')
        note_type = note.get('note_type')
        # note_type =1, html

        dt_object = datetime.fromtimestamp(date_timestamp)
        date = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        note_res = requests.get('https://www.jianshu.com/author/notes/'+str(note.get('id'))+'/content', headers=headers)     
        note = json.loads(note_res.text)
        content = note.get('content')
        if note_type == 1:
            content = markdownify(content)
        f = open(notebook_name+'/'+title.replace('/','-')+'.md', "w")
        title = 'title: ' + title +'\n'
        date = 'date: ' + date +'\n' 
        other = 'categories: 简书\n  --- \n\n\n'
        f.write(title+date+other+content)
        f.close()
