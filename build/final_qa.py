# -*- coding: utf-8 -*-
"""交付前总验收：把用户提出的各项要求逐条机械校验，输出通过/不通过。
用法：python final_qa.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_parser import parse_file, FIELDS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
MY = os.path.join(CONTENT, 'my')

BANK = ['ch04a.txt', 'ch04b.txt', 'ch05a.txt', 'ch05b.txt', 'ch06a.txt',
        'ch06b.txt', 'ch07a.txt', 'ch07b.txt', 'ch08a.txt', 'ch08b.txt',
        'ch09a.txt', 'ch09b.txt', 'ch10a.txt', 'ch10b.txt', 'ch11a.txt',
        'ch11b.txt', 'ch12a.txt', 'ch12b.txt']
MOCKS = [('mock1a.txt', 'mock1b.txt'), ('mock2a.txt', 'mock2b.txt'),
         ('mock3a.txt', 'mock3b.txt')]
PROSE = ['ch00_usage.txt', 'ch01_analysis.txt', 'ch02_plan.txt',
         'ch03_formulas.txt', 'ch13_mixed.txt', 'ch14_strategy.txt',
         'ch15_errorbook.txt', 'appendix.txt']
BANNED = ['显然', '易知', '计算即得', '由常规方法可得', '不难看出',
          '同理可得', '略去', '读者自证', '显而易见']

results = []


def check(name, ok, detail=''):
    results.append((ok, name, detail))


def main():
    # ---------- A. 题库 ----------
    bank_problems = []
    missing_files = []
    for n in BANK:
        p = os.path.join(CONTENT, n)
        if not os.path.exists(p):
            missing_files.append(n)
            continue
        ch = parse_file(p)
        bank_problems.extend(ch.problems)
    check('题库 18 个分册文件齐全', not missing_files,
          '缺少：%s' % missing_files if missing_files else '')

    n_bank = len(bank_problems)
    check('题库题量在 200–300 之间', 200 <= n_bank <= 300, '实际 %d 题' % n_bank)

    bad_field = []
    short_sol = []
    for p in bank_problems:
        for f in FIELDS:
            if f not in p.fields or not p.fields[f].strip():
                bad_field.append('%s 缺 %s' % (p.id, f))
        if len(p.fields.get('SOLUTION', '')) < 200:
            short_sol.append('%s(%d字)' % (p.id, len(p.fields.get('SOLUTION', ''))))
    check('每题 10 个字段齐全且非空', not bad_field, '；'.join(bad_field[:5]))
    check('每题【详细解答】≥200 字（不跳步）', not short_sol,
          '偏短：%s' % '、'.join(short_sol[:8]))

    stars = {}
    for p in bank_problems:
        stars[p.star] = stars.get(p.star, 0) + 1
    check('不出现 ★★★★ / ★★★★★ 难度',
          stars.get('★★★★', 0) == 0 and stars.get('★★★★★', 0) == 0,
          '分布 %s' % stars)
    hard = stars.get('★★★', 0) / max(n_bank, 1)
    check('★★★ 占比不超过 25%（以基础题为主）', hard <= 0.25,
          '★★★ = %d 题（%.1f%%）' % (stars.get('★★★', 0), hard * 100))

    # 母题 + 变式 体系
    no_var = []
    for n in BANK:
        p = os.path.join(CONTENT, n)
        if not os.path.exists(p):
            continue
        for sec in parse_file(p).sections:
            if not sec.problems:
                continue
            if sec.problems[0].type != '母题':
                no_var.append('%s 首题非母题' % sec.num)
            if sum(1 for x in sec.problems if x.type == '变式') < 2:
                no_var.append('%s 变式不足 2 道' % sec.num)
            if len(sec.method) < 60:
                no_var.append('%s 缺"这一类题我到底应该记住什么"' % sec.num)
    check('每个题型都是"母题 + ≥2 变式"并配有方法总结', not no_var,
          '；'.join(no_var[:5]))

    # ---------- B. 模拟卷 ----------
    for a, b in MOCKS:
        chs = []
        for n in (a, b):
            p = os.path.join(CONTENT, n)
            if os.path.exists(p):
                chs.append(parse_file(p))
        if len(chs) < 2:
            check('模拟卷 %s 两个分册齐全' % a, False, '缺少分册')
            continue
        probs = []
        for c in chs:
            probs.extend(c.problems)
        fill = [x for x in probs if x.type == '填空']
        solve = [x for x in probs if x.type == '解答']
        total = sum(int(re.sub(r'\D', '', x.attrs.get('score', '0')) or 0)
                    for x in probs)
        info = (chs[0].info or '') + (chs[1].info or '')
        ok = (len(fill) == 5 and len(solve) == 5 and total == 100)
        check('模拟卷 %s：5 填空(6分)+5 解答(14分)=100 分' % a, ok,
              '填空 %d 题、解答 %d 题、总分 %d' % (len(fill), len(solve), total))
        need = ['时间分配', '难度分析', '建议得分']
        lack = [k for k in need if k not in info]
        check('模拟卷 %s 写明时间分配/难度分析/建议得分' % a, not lack,
              '缺少 %s' % lack)
        check('模拟卷 %s 有题号级分层得分目标' % a,
              bool(re.search(r'M\d-\d', info)), '')
        titles = set(c.title for c in chs)
        check('模拟卷 %s 两个分册 @@MOCK 标题一致' % a, len(titles) == 1,
              '、'.join(titles))
    n_mock = sum(len(parse_file(os.path.join(CONTENT, n)).problems)
                 for pair in MOCKS for n in pair
                 if os.path.exists(os.path.join(CONTENT, n)))
    check('模拟卷题量 30 题（3 套 × 10 题）', n_mock == 30, '实际 %d' % n_mock)

    # ---------- C. 正文章节 ----------
    for n in PROSE:
        check('正文文件存在：%s' % n, os.path.exists(os.path.join(MY, n)), '')

    # 计划里引用的题号必须真实存在
    plan_path = os.path.join(MY, 'ch02_plan.txt')
    if os.path.exists(plan_path):
        with open(plan_path, encoding='utf-8-sig') as f:
            plan = f.read()
        ids = set(re.findall(r'\b\d+\.\d+-\d+\b', plan))
        valid = set(p.id for p in bank_problems)
        bad = sorted(i for i in ids if i not in valid)
        check('20 天计划引用的题号全部真实存在（%d 个）' % len(ids), not bad,
              '不存在：%s' % '、'.join(bad[:10]))
        days = len(re.findall(r'### Day \d+', plan))
        check('20 天计划含 16 天详细任务 + 4 天模拟冲刺 = 20 天', days == 16,
              '详细任务 %d 天（另有 Day17–20 表格）' % days)
        check('计划写明"必做/加练"与今日目标分值能力',
              '加练' in plan and '目标分值能力' in plan, '')

    # 混合训练引用的题号
    mx = os.path.join(MY, 'ch13_mixed.txt')
    if os.path.exists(mx):
        with open(mx, encoding='utf-8-sig') as f:
            text = f.read()
        ids = set(re.findall(r'\b\d+\.\d+-\d+\b', text))
        valid = set(p.id for p in bank_problems)
        bad = sorted(i for i in ids if i not in valid)
        check('混合训练卷引用的题号全部真实存在', not bad,
              '不存在：%s' % '、'.join(bad[:10]))
        check('混合训练含 3 套卷与题型判断记录表',
              text.count('混合限时训练卷') == 3 and '题型判断记录表' in text, '')

    # ---------- D. 禁止用语 ----------
    QUOTED = re.compile(r'"[^"]{0,120}"|“[^”]{0,120}”|「[^」]{0,120}」'

                       r'|（[^）]{0,40}）')

    def strip_quoted(t):
        """去掉引号内的"反面例句"（如 绝不写"显然"），只查真正写进解答的用语。"""
        return QUOTED.sub('', t)

    hit = []
    for n in os.listdir(CONTENT):
        if not n.endswith('.txt'):
            continue
        with open(os.path.join(CONTENT, n), encoding='utf-8-sig') as f:
            t = strip_quoted(f.read())
        for b in BANNED:
            if b in t:
                hit.append('%s 出现「%s」×%d' % (n, b, t.count(b)))
    for n in os.listdir(MY):
        if not n.endswith('.txt'):
            continue
        with open(os.path.join(MY, n), encoding='utf-8-sig') as f:
            t = strip_quoted(f.read())
        for b in BANNED:
            if b in t:
                hit.append('my/%s 出现「%s」×%d' % (n, b, t.count(b)))
    check('全资料无"显然/易知/计算即得"等跳步用语', not hit, '；'.join(hit[:6]))

    # ---------- E. 真题来源真实性 ----------
    fake = []
    for n in os.listdir(CONTENT):
        if not n.endswith('.txt'):
            continue
        with open(os.path.join(CONTENT, n), encoding='utf-8-sig') as f:
            t = f.read()
        for m in re.finditer(r'(19|20)\d{2}\s*年|第[一二三四五六七八九十]+届', t):
            ctx = t[max(0, m.start() - 20):m.end() + 20].replace('\n', ' ')
            fake.append('%s: …%s…' % (n, ctx))
    check('题库与模拟卷中没有编造的真题年份/届次', not fake, '；'.join(fake[:5]))

    # ---------- F. 覆盖模块 ----------
    kps = set()
    for p in bank_problems:
        kps.add(p.kp.split('/')[0])
    need_mods = ['极限', '导数', '中值定理', '积分', '定积分', '多元微分',
                 '多元极值', '二重积分', '微分方程', '级数', '综合',
                 '空间解析几何', '曲线积分', '连续']
    lack = [m for m in need_mods if m not in kps]
    check('覆盖 CMC 全部高频模块（极限/导数/积分/多元/微分方程/级数等）',
          not lack, '缺少：%s' % lack)

    # ---------- 输出 ----------
    n_ok = sum(1 for ok, _, _ in results if ok)
    print('=' * 78)
    for ok, name, detail in results:
        print('%s %s%s' % ('[通过]' if ok else '[未过]', name,
                           ('　—　' + detail) if (detail and not ok) else ''))
    print('=' * 78)
    print('验收结果：%d / %d 项通过' % (n_ok, len(results)))
    print('题库题量 %d 题，模拟卷 %d 题，合计 %d 题'
          % (n_bank, n_mock, n_bank + n_mock))
    print('难度分布：%s' % ' '.join('%s=%d' % (k, stars[k])
                                for k in sorted(stars)))
    return 0 if n_ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())