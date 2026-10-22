# -*- coding: utf-8 -*-
"""列出 docx 里的一级/二级标题顺序，检查章节结构是否符合要求。"""
import re
import sys
import zipfile
from collections import Counter

path = sys.argv[1]
with zipfile.ZipFile(path) as z:
    xml = z.read('word/document.xml').decode('utf-8')

paras = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
h1 = []
h2 = 0
n_tbl = len(re.findall(r'<w:tbl>', xml))
for p in paras:
    m = re.search(r'<w:pStyle w:val="(Heading[1-3]|标题[1-3]?)"', p)
    if not m:
        continue
    style = m.group(1)
    txt = ''.join(re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>', p, re.S))
    txt = re.sub(r'<[^>]+>', '', txt)
    if style in ('Heading1', '标题1', '标题 1'):
        h1.append(txt.strip())
    elif style in ('Heading2', '标题2', '标题 2'):
        h2 += 1
print('一级标题共 %d 个，二级标题共 %d 个，表格 %d 个' % (len(h1), h2, n_tbl))
for t in h1:
    print('  %s' % t)