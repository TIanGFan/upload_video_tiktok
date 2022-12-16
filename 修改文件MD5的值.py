#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'
import hashlib
import os

"""
查看文件md5值
with open("./video/my_0.mp4", "rb") as file:
    md5_ojb = hashlib.md5()
    while True:
        buffer = file.read(8096)
        if not buffer:
            break
        md5_ojb.update(buffer)
    hash_code = md5_ojb.hexdigest()
    md5 = str(hash_code).lower()
    "70afde3147748f1c7126c1dacb96369c"
    print(md5)
"""

# 修改文件md5的值
video_path = r'C:\Users\Administrator\Desktop\DOUYIN_video\video\善喜说女装--110567985801'

for i in os.listdir(video_path):
    file_name = os.path.join(video_path, i)
    with open(file_name, "a") as f:
        f.write("####&&&&")
        print("{} 文件的 MD5 值修改成功".format(i))
