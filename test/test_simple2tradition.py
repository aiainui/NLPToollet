#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 简繁体转换代码
import os
import sys
sys.path.append('../tool/font_conversion/')
from langconv import *

def simple2tradition(line):
    # 将简体转换成繁体
    #line = Converter('zh-hant').convert(line.decode('utf-8'))
    #line = line.encode('utf-8')
    line = Converter('zh-hant').convert(line)
    line = line
    return line

tx = u"输入简体字,点下面繁体字按钮进行在线转换"
res = simple2tradition(tx)
print(res)
