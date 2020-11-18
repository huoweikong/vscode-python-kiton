import requests
import re

headers = {
    'Referer': 'https://lol.qq.com/data/info-defail.shtml?id=Aatrox',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

response = requests.get('https://lol.qq.com/biz/hero/champion.js', headers=headers)
keys = re.findall(r'"keys":{(.*?)},"data"',response.text,re.S)
keys = keys[0]
keys = keys.split(',')

with open('hero','w') as f:
    for key in keys:
        f.write(key)
        f.write('\n')
        print(key)