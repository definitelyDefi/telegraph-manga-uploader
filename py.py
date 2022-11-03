
from telegraph import Telegraph

import requests
import os

directory = 'img'

telegraph = Telegraph()
telegraph.create_account(short_name='definitelydefi')
html_content = ""
title = input('Type title of article: ')


if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    
    if os.path.isfile(file):
        with open(file, 'rb') as f:

            print(f'[~] Proccesing {os.path.basename(file)}')
            json_data = requests.post('https://telegra.ph/upload', files={'file': ('file', f,'image/jpeg')}).json()[0]['src']
            html_content += f'<img src="{json_data}">'
            f.close()

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    os.remove(file)

print('[-] Files deleted')
    


response = telegraph.create_page(
    title,
    html_content=html_content
)



print('[+] Link: http://telegra.ph/{}'.format(response['path']))