#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'
import time

import pyperclip as pyperclip
from tqdm import tqdm, trange

m = [100]
for i in tqdm(m):
    time.sleep(1)

for i in range(15):
    time.sleep(0.5)  # 这里为了查看输出变化，实际使用不需要sleep
    print('\r', "上传进度为 {} ".format(i), end='')
    print('\r', "上传进度为111111 {} ".format(i), end='')
    # print('\r', 15-i, end='') # 从两位变一位会有问题

str_1 = "Ability is what you're capable of doing. Motivation determines what you do. Attitude determines how well you do i"
pyperclip.copy(str_1)

# text = pyperclip.paste()

