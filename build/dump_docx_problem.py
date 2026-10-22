# -*- coding: utf-8 -*-
"""从生成的 docx 里抽出指定题号的完整段落文本，检查字段顺序与内容是否按要求呈现。
用法：python dump_docx_problem.py <docx> <题号，如 4.1-1>
"""
import re
import sys
import zipfile

path, pid = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(path) as z:
    xml = z.read('word/document.xml').decode('utf-8')

# 按段落切分
paras = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
texts = []
for p in paras:
    runs = re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>', p, re.S)
    s = ''.join(runs)
    s = s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    n_math = len(re.findall(r'<m:oMath[ >]', p))
    if s.strip() or n_math:
        texts.append((s.strip(), n_math))

start = None
for i, (s, n) in enumerate(texts):
    if s.startswith('题 %s' % pid):
        start = i
        break
if start is None:
    print('未找到题号 %s' % pid)
    sys.exit(1)
print('=== 题 %s 在 Word 中的实际呈现（[公式n] 表示该段含 n 个原生公式）===' % pid)
for s, n in texts[start:start + 22]:
    tag = '[公式%d]' % n if n else ''
    print('%s%s' % (s[:110], tag))
    print('-' * 70)