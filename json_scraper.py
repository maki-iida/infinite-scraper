# coding: UTF-8

import requests
import base64

url = 'https://qiita.com/___xxx_'
res = requests.get('http://localhost:8050/render.json',
                   params={'url': url, 'wait': 0.5, 'html': 1, 'jpeg': 1, 'height': 800})

data = res.json()

# ページタイトル
print(data['title'])

# htmlファイルを保存
with open('json.html', 'w') as f:
    f.write(data['html'].encode('utf_8'))

# jpegファイルを保存
jpeg_data = base64.b64decode(data['jpeg'].encode())
with open('json.jpg', 'wb') as f:
    f.write(jpeg_data)
