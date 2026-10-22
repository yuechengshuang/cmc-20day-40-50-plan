# -*- coding: utf-8 -*-
"""打印每道题的 id / 难度 / 知识点 / 答案，用于快速人工抽查。"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_parser import parse_file

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')

names = sys.argv[1:] or sorted(n for n in os.listdir(CONTENT)
                               if n.endswith('.txt') and not n.startswith('zz_'))


def one(t):
    t = re.sub(r'\s+', ' ', t).strip()
    for m in re.finditer(r'\$\$(.+?)\$\$|\$(.+?)\$', t):
        pass
    return t[:90]


for n in names:
    path = os.path.join(CONTENT, n)
    if not os.path.exists(path):
        continue
    ch = parse_file(path)
    print('=' * 92)
    print('%s  (%s)' % (n, ch.title))
    for p in ch.problems:
        print('%-8s %-4s %-22s %s' % (p.id, p.star, p.kp[:22],
                                      one(p.fields.get('ANSWER', ''))))