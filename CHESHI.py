#!/usr/bin/env python
# -*- coding: utf-8 -*
# __author__ = 'LIUTIANFAN'

import time
from SqlData import GetId, GetTitle, Delete, SvsaId

print(GetId())
time.sleep(3)

title = GetTitle(GetId())
time.sleep(3)

# print(title[1])
# Delete(GetId())
# time.sleep(3)

# print(title[1])
# SvsaId(GetId())
