# -*- coding: utf-8 -*-
"""解析 content/*.txt（@@ 标记格式）为结构化对象。"""
import os
import re

FIELDS = ['STEM', 'POINT', 'IDENTIFY', 'FORMULAS', 'IDEA', 'SOLUTION',
          'ANSWER', 'PITFALL', 'TIPS', 'SUMMARY']

FIELD_LABEL = {
    'STEM': '题目', 'POINT': '考查知识点', 'IDENTIFY': '题型识别',
    'FORMULAS': '需要记住的公式', 'IDEA': '解题思路', 'SOLUTION': '详细解答',
    'ANSWER': '最终答案', 'PITFALL': '易错点', 'TIPS': '同类题识别技巧',
    'SUMMARY': '一句话总结',
}


class ParseError(Exception):
    pass


class Problem(object):
    def __init__(self, attrs, line_no):
        self.attrs = attrs
        self.line_no = line_no
        self.fields = {}
        self.id = attrs.get('id', '')
        self.type = attrs.get('type', '')
        self.star = attrs.get('star', '')
        self.time = attrs.get('time', '')
        self.imp = attrs.get('imp', '')
        self.kp = attrs.get('kp', '')

    @property
    def star_count(self):
        return self.star.count('★')


class Section(object):
    def __init__(self, num, title, line_no):
        self.num = num
        self.title = title
        self.line_no = line_no
        self.method = ''
        self.problems = []

    @property
    def full_title(self):
        return (self.num + ' ' + self.title).strip()


class Chapter(object):
    def __init__(self, path):
        self.path = path
        self.title = ''
        self.guide = ''
        self.sections = []
        self.is_mock = False
        self.info = ''

    @property
    def problems(self):
        out = []
        for s in self.sections:
            out.extend(s.problems)
        return out


def _attr_parse(rest, path, line_no):
    attrs = {}
    for m in re.finditer(r'(\w+)\s*=\s*([^=]*?)(?=\s+\w+\s*=|$)', rest):
        attrs[m.group(1)] = m.group(2).strip()
    if not attrs:
        raise ParseError('%s:%d @@PROBLEM 行缺少属性' % (path, line_no))
    return attrs


def parse_file(path):
    with open(path, encoding='utf-8-sig') as f:
        lines = f.read().replace('\r\n', '\n').replace('\r', '\n').split('\n')

    ch = Chapter(path)
    cur_sec = None
    cur_prob = None
    state = None          # 'GUIDE' | 'METHOD' | field name
    buf = []

    def flush():
        nonlocal buf, state
        content = '\n'.join(buf).strip()
        if state == 'GUIDE':
            ch.guide = content
        elif state == 'INFO':
            ch.info = content
        elif state == 'METHOD':
            if cur_sec is None:
                raise ParseError('%s: @@METHOD 出现在 @@SECTION 之前' % path)
            cur_sec.method = content
        elif state in FIELDS:
            if cur_prob is None:
                raise ParseError('%s: %s 出现在 @@PROBLEM 之外' % (path, state))
            if state in cur_prob.fields:
                raise ParseError('%s: 题目 %s 字段 %s 重复' % (path, cur_prob.id, state))
            cur_prob.fields[state] = content
        buf = []
        state = None

    for idx, raw in enumerate(lines, 1):
        line = raw.rstrip()
        if line.startswith('@@'):
            cmd = line[2:].strip()
            word = cmd.split(' ', 1)[0].strip()
            rest = cmd[len(word):].strip()
            if word == 'CHAPTER':
                flush()
                ch.title = rest
            elif word == 'MOCK':
                flush()
                ch.title = rest
                ch.is_mock = True
            elif word == 'INFO':
                flush()
                state = 'INFO'
            elif word == 'INFOEND':
                flush()
            elif word == 'GUIDE':
                flush()
                state = 'GUIDE'
            elif word == 'GUIDEEND':
                flush()
            elif word == 'SECTION':
                flush()
                m = re.match(r'^([\d.]+)\s+(.*)$', rest)
                if m:
                    cur_sec = Section(m.group(1), m.group(2), idx)
                else:
                    cur_sec = Section('', rest, idx)
                ch.sections.append(cur_sec)
            elif word == 'METHOD':
                flush()
                state = 'METHOD'
            elif word == 'METHODEND':
                flush()
            elif word == 'PROBLEM':
                flush()
                attrs = _attr_parse(rest, path, idx)
                cur_prob = Problem(attrs, idx)
                if cur_sec is None:
                    if not ch.is_mock:
                        raise ParseError('%s:%d 题目出现在 @@SECTION 之前' % (path, idx))
                    cur_sec = Section('', '本卷题目', idx)
                    ch.sections.append(cur_sec)
                cur_sec.problems.append(cur_prob)
            elif word == 'ENDPROBLEM':
                flush()
                cur_prob = None
            elif word in FIELDS:
                flush()
                state = word
            else:
                raise ParseError('%s:%d 未知标记 @@%s' % (path, idx, word))
        else:
            if state is not None:
                buf.append(line)
            elif line.strip():
                raise ParseError('%s:%d 正文出现在任何标记之外：%s'
                                 % (path, idx, line[:40]))
    flush()
    return ch


def load_dir(folder):
    chapters = []
    for name in sorted(os.listdir(folder)):
        if name.endswith('.txt'):
            chapters.append(parse_file(os.path.join(folder, name)))
    return chapters