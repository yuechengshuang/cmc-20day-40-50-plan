# -*- coding: utf-8 -*-
"""内容文件格式 + 公式 + 用语 自检工具。

用法：
  python check_content.py <file.txt> [more.txt ...]
  python check_content.py --dir <content目录>
退出码 0 = 全部通过。
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_parser import parse_file, FIELDS, ParseError
from latex_omml import omml_element

MATH_RE = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)
BANNED = ['显然', '易知', '计算即得', '由常规方法可得', '不难看出', '同理可得',
          '（略）', '(略)', '略去', '读者自证', '显而易见', '容易得到', '直接可得']
VALID_STAR = {'★', '★★', '★★★', '★★★★', '★★★★★'}
VALID_TYPE = {'母题', '变式', '基础训练', '提高训练'}
VALID_IMP = {'★★★★★', '★★★★', '★★★', '★★'}


def collect_math(text):
    """返回 (公式列表, 剩余非公式文本)"""
    formulas = []
    for m in MATH_RE.finditer(text):
        formulas.append(m.group(1) if m.group(1) is not None else m.group(2))
    stripped = MATH_RE.sub('', text)
    return formulas, stripped


def check_file(path, verbose=True):
    errors = []
    warns = []
    try:
        ch = parse_file(path)
    except ParseError as e:
        return ['解析失败：%s' % e], [], None
    except Exception as e:
        return ['文件读取失败：%r' % e], [], None

    name = os.path.basename(path)
    if not ch.title:
        errors.append('缺少 @@CHAPTER 标题')
    if ch.is_mock:
        if len(ch.info) < 150:
            errors.append('模拟卷 @@INFO 过短（至少写清时间分配、难度分析、分层目标、建议得分）')
    elif len(ch.guide) < 80:
        warns.append('本文件没有 @@GUIDE（若同章的 a 分册已提供拿分指南，则正常）')
    if not ch.sections:
        errors.append('没有任何 @@SECTION')

    ids = {}
    n_prob = 0
    n_math = 0
    math_fail = []
    nary_cnt = {'★': 0, '★★': 0, '★★★': 0, '★★★★': 0}

    for sec in ch.sections:
        if ch.is_mock:
            if not sec.problems:
                errors.append('模拟卷没有题目')
                continue
        else:
            if not sec.method:
                errors.append('题型 %s 缺少 @@METHOD ... @@METHODEND' % sec.full_title)
            elif len(sec.method) < 60:
                warns.append('题型 %s 的 @@METHOD 偏短（%d 字）' % (sec.full_title, len(sec.method)))
            if not sec.problems:
                errors.append('题型 %s 下没有题目' % sec.full_title)
                continue
            if sec.problems[0].type != '母题':
                errors.append('题型 %s 的第 1 题必须是 type=母题，现在是 %s'
                              % (sec.full_title, sec.problems[0].type or '空'))
            n_var = sum(1 for p in sec.problems if p.type == '变式')
            if n_var < 2:
                warns.append('题型 %s 只有 %d 道变式题（建议 2~4 道）' % (sec.full_title, n_var))

        for p in sec.problems:
            n_prob += 1
            tag = '%s [%s]' % (p.id or '(无id)', sec.full_title)
            if not p.id:
                errors.append('题目缺少 id=%s' % tag)
            elif p.id in ids:
                errors.append('题目 id 重复：%s' % p.id)
            else:
                ids[p.id] = True
            if ch.is_mock:
                if p.type not in ('填空', '解答'):
                    errors.append('%s 模拟卷题目 type 必须是 填空 或 解答，现在是 %r' % (tag, p.type))
                sc = p.attrs.get('score', '')
                if not re.match(r'^\d+分?$', sc or ''):
                    errors.append('%s 缺少合法的 score=（如 score=6）' % tag)
            elif p.type not in VALID_TYPE:
                errors.append('%s type 非法：%r（应为 母题/变式/基础训练/提高训练）' % (tag, p.type))
            if p.star not in VALID_STAR:
                errors.append('%s star 非法：%r' % (tag, p.star))
            else:
                nary_cnt[p.star] = nary_cnt.get(p.star, 0) + 1
            if not re.match(r'^\d+分钟$', p.time or ''):
                errors.append('%s time 非法：%r（应形如 6分钟）' % (tag, p.time))
            if p.imp not in VALID_IMP:
                errors.append('%s imp 非法：%r' % (tag, p.imp))
            if not p.kp:
                errors.append('%s 缺少 kp=' % tag)

            for f in FIELDS:
                if f not in p.fields:
                    errors.append('%s 缺少字段 @@%s' % (tag, f))
                elif not p.fields[f].strip():
                    errors.append('%s 字段 @@%s 为空' % (tag, f))

            if 'SOLUTION' in p.fields and len(p.fields['SOLUTION']) < 100:
                errors.append('%s 的【详细解答】只有 %d 字，太短，必须写出中间步骤'
                              % (tag, len(p.fields['SOLUTION'])))
            if 'FORMULAS' in p.fields:
                fl = [x for x in p.fields['FORMULAS'].split('\n') if x.strip()]
                if len(fl) < 1:
                    errors.append('%s 的【需要记住的公式】为空' % tag)
            for f in ('STEM', 'ANSWER'):
                if f in p.fields and len(p.fields[f].strip()) < 2:
                    errors.append('%s 的 @@%s 过短' % (tag, f))

            all_text = '\n'.join(p.fields.get(f, '') for f in FIELDS)
            formulas, stripped = collect_math(all_text)
            if '$' in stripped:
                errors.append('%s 存在未配对的 $ 号' % tag)
            n_math += len(formulas)
            for fm in formulas:
                try:
                    omml_element(fm, display=False)
                    omml_element(fm, display=True)
                except Exception as e:
                    math_fail.append((tag, fm[:60], str(e)[:70]))

            for b in BANNED:
                if b in all_text:
                    errors.append('%s 出现禁止用语「%s」' % (tag, b))

            # 独立公式行必须是 $$..$$ 独占一行
            for ln in all_text.split('\n'):
                if '$$' in ln and not ln.strip().startswith('$$'):
                    warns.append('%s 的 $$ 公式行混有正文：%s' % (tag, ln.strip()[:40]))

    if verbose:
        print('文件：%s' % name)
        print('  章节：%s' % (ch.title or '(无)'))
        print('  题型数：%d，题目数：%d，公式数：%d' % (len(ch.sections), n_prob, n_math))
        print('  难度分布：' + '  '.join('%s=%d' % (k, nary_cnt.get(k, 0))
                                        for k in ['★', '★★', '★★★', '★★★★']))
        if math_fail:
            print('  公式解析失败 %d 处：' % len(math_fail))
            for tag, fm, err in math_fail[:15]:
                print('    - %s | %s | %s' % (tag, fm, err))
        if warns:
            print('  提醒 %d 条：' % len(warns))
            for w in warns[:12]:
                print('    ! %s' % w)
        if errors:
            print('  错误 %d 条：' % len(errors))
            for e in errors[:40]:
                print('    x %s' % e)
        else:
            print('  >>> 格式检查通过（公式解析 0 处失败，禁止用语 0 处）')
    return errors, warns, (n_prob, n_math)


def main():
    args = sys.argv[1:]
    files = []
    if args and args[0] == '--dir':
        folder = args[1]
        files = [os.path.join(folder, n) for n in sorted(os.listdir(folder))
                 if n.endswith('.txt')]
    else:
        files = args
    if not files:
        print('用法：check_content.py <file.txt> | --dir <目录>')
        return 2
    total_err = 0
    total_prob = 0
    for f in files:
        errs, warns, stat = check_file(f)
        if stat:
            total_prob += stat[0]
        total_err += len(errs)
        print('')
    print('=' * 60)
    print('合计：%d 个文件，%d 道题，错误 %d 条' % (len(files), total_prob, total_err))
    return 1 if total_err else 0


if __name__ == '__main__':
    sys.exit(main())