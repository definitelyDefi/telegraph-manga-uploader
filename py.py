from telegraph import Telegraph
import requests
import os

directory = 'img'

telegraph = Telegraph()
telegraph.create_account(short_name='definitelydefi')
html_content = ""
title = input('Type title of article: ')

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        print(f'[~] Proccesing {os.path.basename(file)}')
        with open(file, 'rb') as f:
            path = requests.post('https://telegra.ph/upload', files={'file': ('file', f,'image/jpeg')}).json()[0]['src']
        
        html_content += f'<img src="{path}">'
        os.remove(file)

response = telegraph.create_page(
    title,
    html_content=html_content
)



print('[+] http://telegra.ph/{}'.format(response['path']))