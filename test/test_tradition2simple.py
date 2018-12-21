#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('../tool/font_conversion/')
from langconv import *

def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line)
    line = line
    return line

tx = u"蝴蝶飛起我敏感的心情 在汗水之間輕劃過一道虹漪"
res = tradition2simple(tx)
print(res)
