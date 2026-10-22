# -*- coding: utf-8 -*-
"""打印 docx 最前面若干段的文本（检查封面/目录区）。"""
import re
import sys
import zipfile

path = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 14
with zipfile.ZipFile(path) as z:
    xml = z.read('word/document.xml').decode('utf-8')
paras = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
out = 0
for p in paras:
    txt = ''.join(re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>', p, re.S))
    txt = txt.replace('&amp;', '&')
    if txt.strip():
        print(repr(txt.strip())[1:-1])
        out += 1
        if out >= n:
            break