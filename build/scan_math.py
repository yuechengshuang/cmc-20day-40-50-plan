# -*- coding: utf-8 -*-
"""扫描所有内容文件里的公式，统计转换失败的公式与其中用到的未知命令。
用法：python scan_math.py [目录]
"""
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from latex_omml import omml_element

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'content')
MATH_RE = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)
CMD_RE = re.compile(r'\\([A-Za-z]+)')


def iter_math(text):
    for m in MATH_RE.finditer(text):
        yield m.group(1) if m.group(1) is not None else m.group(2)


def main():
    files = []
    for base, _dirs, names in os.walk(FOLDER):
        for n in sorted(names):
            if n.endswith('.txt'):
                files.append(os.path.join(base, n))
    total = 0
    fails = []
    cmd_counter = Counter()
    file_counter = Counter()
    for path in files:
        with open(path, encoding='utf-8-sig') as f:
            text = f.read()
        for fm in iter_math(text):
            total += 1
            try:
                omml_element(fm, display=False)
                omml_element(fm, display=True)
            except Exception as e:
                fails.append((os.path.basename(path), fm, str(e)[:80]))
                file_counter[os.path.basename(path)] += 1
                for c in CMD_RE.findall(fm):
                    cmd_counter[c] += 1
    print('公式总数：%d，失败：%d' % (total, len(fails)))
    if cmd_counter:
        print('\n失败公式中出现的命令（按次数）：')
        for c, n in cmd_counter.most_common(40):
            print('   \\%s  ×%d' % (c, n))
    if file_counter:
        print('\n按文件统计失败数：')
        for f, n in file_counter.most_common():
            print('   %-22s %d' % (f, n))
    print('\n前 25 条失败样例：')
    for f, fm, e in fails[:25]:
        print('  [%s] %s  ->  %s' % (f, fm[:70], e))


if __name__ == '__main__':
    main()