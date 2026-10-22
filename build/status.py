# -*- coding: utf-8 -*-
"""题库完整性看板：按章统计题型、题数、难度分布，并列出缺失的计划题型。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_parser import parse_file

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')

PLAN = {
    '第四章 极限与连续（专项题库）': ['4.1', '4.2', '4.3', '4.4', '4.5', '4.6'],
    '第五章 导数、微分与中值定理（专项题库）': ['5.1', '5.2', '5.3', '5.4', '5.5', '5.6'],
    '第六章 一元函数积分学（专项题库）': ['6.1', '6.2', '6.3', '6.4', '6.5', '6.6'],
    '第七章 定积分应用与积分综合（专项题库）': ['7.1', '7.2', '7.3', '7.4'],
    '第八章 多元函数微分学（专项题库）': ['8.1', '8.2', '8.3', '8.4', '8.5'],
    '第九章 多元函数极值与二重积分（专项题库）': ['9.1', '9.2', '9.3', '9.4', '9.5'],
    '第十章 常微分方程（专项题库）': ['10.1', '10.2', '10.3', '10.4', '10.5', '10.6'],
    '第十一章 无穷级数（专项题库）': ['11.1', '11.2', '11.3', '11.4', '11.5'],
    '第十二章 其他高频基础题型与送分模块（专项题库）': ['12.1', '12.2', '12.3', '12.4', '12.5'],
}

names = sorted(n for n in os.listdir(CONTENT) if n.endswith('.txt')
               and not n.startswith('zz_'))
chapters = {}
titles = {}
for n in names:
    ch = parse_file(os.path.join(CONTENT, n))
    if ch.is_mock:
        chapters.setdefault('MOCK:' + ch.title, []).append(ch)
        continue
    chapters.setdefault(ch.title, []).append(ch)
    titles.setdefault(ch.title, set()).add(n)

total = 0
star_total = {}
for title, chs in sorted(chapters.items()):
    if title.startswith('MOCK:'):
        n = sum(len(c.problems) for c in chs)
        print('%-30s 模拟卷题数 %d  %s' % (title[5:], n, '、'.join(sorted(
            f for f in os.listdir(CONTENT) if f.startswith('mock')))))
        total += n
        continue
    secs = {}
    for c in chs:
        for s in c.sections:
            secs.setdefault(s.num, []).extend(s.problems)
    n = sum(len(v) for v in secs.values())
    total += n
    dist = {}
    for v in secs.values():
        for p in v:
            dist[p.star] = dist.get(p.star, 0) + 1
            star_total[p.star] = star_total.get(p.star, 0) + 1
    missing = [s for s in PLAN.get(title, []) if s not in secs]
    print('=' * 78)
    print('%s' % title)
    print('  文件：%s' % '、'.join(sorted(titles.get(title, []))))
    print('  题型 %d 个，题目 %d 道，难度 %s' % (
        len(secs), n, ' '.join('%s=%d' % (k, dist[k]) for k in sorted(dist))))
    for s in sorted(secs, key=lambda x: [int(y) for y in x.split('.')]):
        ps = secs[s]
        first = next((c for c in chs for sec in c.sections if sec.num == s), None)
        t = next((sec.title for c in chs for sec in c.sections if sec.num == s), '')
        ids = '%s..%s' % (ps[0].id, ps[-1].id)
        print('    %-6s %-34s %2d 题  %s' % (s, t[:34], len(ps), ids))
    if missing:
        print('  !! 缺失题型：%s' % '、'.join(missing))
print('=' * 78)
print('题库合计：%d 道题' % total)
print('难度分布：%s' % ' '.join('%s=%d' % (k, star_total[k])
                            for k in sorted(star_total)))