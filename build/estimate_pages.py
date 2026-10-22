# -*- coding: utf-8 -*-
"""按排版参数估算 docx 页数（A4、左右边距 2cm、正文 10.5pt、行距 1.15）。"""
import math
import re
import sys
import zipfile

path = sys.argv[1]
with zipfile.ZipFile(path) as z:
    xml = z.read('word/document.xml').decode('utf-8')

paras = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
USABLE_CM = 21.0 - 2.0 - 2.0          # 17 cm 正文宽度
LINE_CM = 0.53                        # 10.5pt + 1.15 行距的一行高度
USABLE_H = 29.7 - 2.2 - 2.0           # 25.5 cm
LINES_PER_PAGE = USABLE_H / LINE_CM

total_lines = 0.0
n_display = 0
for p in paras:
    texts = re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>', p, re.S)
    s = ''.join(texts)
    n_math = len(re.findall(r'<m:oMath[ >]', p))
    is_display = '<m:oMathPara' in p
    cjk = len(re.findall(r'[\u3000-\u9fff\uff00-\uffef]', s))
    other = len(s) - cjk
    width = cjk * 1.0 + other * 0.55 + n_math * 2.2     # 以"汉字宽"为单位
    if is_display:
        n_display += 1
        total_lines += 1.6                              # 独立公式行更占高
        continue
    if width == 0:
        total_lines += 0.35                             # 空段
        continue
    total_lines += max(1.0, math.ceil(width / 39.0) * 1.0) + 0.22

pages = total_lines / LINES_PER_PAGE
print('段落数            %d' % len(paras))
print('独立公式行        %d' % n_display)
print('估算正文行数      %.0f' % total_lines)
print('每页行数（估）    %.0f' % LINES_PER_PAGE)
print('估算页数          %.0f 页' % pages)