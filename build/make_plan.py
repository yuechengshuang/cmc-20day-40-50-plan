# -*- coding: utf-8 -*-
"""根据已生成的题库，自动生成：
   content/my/ch02_plan.txt      第二章 20天冲刺路线（每日计划引用真实题号）
   content/my/ch13_mixed.txt     第十三章 混合限时训练（真题干打乱，含题型判断记录表）
   content/my/appendix.txt       附录 A 打卡表 / B 考前清单 / C 常见计算失误
用法：python make_plan.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_parser import parse_file

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
MY = os.path.join(CONTENT, 'my')

FILES = ['ch04a.txt', 'ch04b.txt', 'ch05a.txt', 'ch05b.txt', 'ch06a.txt',
         'ch06b.txt', 'ch07a.txt', 'ch07b.txt', 'ch08a.txt', 'ch08b.txt',
         'ch09a.txt', 'ch09b.txt', 'ch10a.txt', 'ch10b.txt', 'ch11a.txt',
         'ch11b.txt', 'ch12a.txt', 'ch12b.txt']

TYPE_ORDER = {'母题': 0, '变式': 1, '基础训练': 2, '提高训练': 3}

# ------------------------------------------------------------------ 每日安排
DAYS = [
    (1, '极限（一）：等价无穷小与洛必达法则', ['4.1', '4.2'],
     ['$\\sin u\\sim u$，$\\tan u\\sim u$，$\\arcsin u\\sim u$，$\\arctan u\\sim u$（$u\\to 0$）',
      '$1-\\cos u\\sim\\frac{u^2}{2}$，$\\ln(1+u)\\sim u$，$e^u-1\\sim u$，$(1+u)^{\\alpha}-1\\sim\\alpha u$',
      '洛必达法则的适用条件：$\\frac00$ 或 $\\frac\\infty\\infty$ 型，且 $\\lim\\frac{f\'}{g\'}$ 存在'],
     '把等价无穷小替换表默写到 100% 正确；看到 $\\frac00$ 型能立刻判断该用等价无穷小还是洛必达'),
    (2, '极限（二）：两个重要极限与夹逼准则', ['4.3', '4.4'],
     ['$\\lim_{x\\to 0}\\frac{\\sin x}{x}=1$，$\\lim_{x\\to\\infty}\\left(1+\\frac1x\\right)^x=e$',
      '$1^\\infty$ 型：原式 $=e^{\\lim(\\text{底}-1)\\times\\text{指数}}$',
      '夹逼准则：$g(x)\\le f(x)\\le h(x)$ 且两端极限相等，则中间极限也等于它'],
     '会处理 $1^\\infty$ 型极限；会用夹逼准则做 $n$ 项和型数列极限'),
    (3, '极限（三）：数列极限与函数的连续性', ['4.5', '4.6'],
     ['单调有界准则：单调增且有上界（或单调减且有下界）的数列必收敛',
      '连续的定义：$\\lim_{x\\to x_0}f(x)=f(x_0)$（左极限 = 右极限 = 函数值）',
      '间断点分类：可去（左右极限存在且相等）、跳跃（左右极限存在不等）、无穷、振荡'],
     '会判断分段函数分界点的连续性；会给间断点分类'),
    (4, '导数（一）：导数定义与各种求导法', ['5.1', '5.2'],
     ['导数定义：$f\'(x_0)=\\lim_{x\\to x_0}\\frac{f(x)-f(x_0)}{x-x_0}$',
      '可导 $\\Rightarrow$ 连续，反之不成立',
      '隐函数求导：方程两边对 $x$ 求导，$y$ 看成 $x$ 的函数',
      '参数方程：$\\frac{dy}{dx}=\\frac{y\'(t)}{x\'(t)}$，$\\frac{d^2y}{dx^2}=\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right)\\div x\'(t)$'],
     '会用定义求分段函数在分界点的导数；隐函数与参数方程求导不出错'),
    (5, '导数（二）：高阶导数与中值定理', ['5.3', '5.4'],
     ['莱布尼茨公式：$(uv)^{(n)}=\\sum_{k=0}^{n}C_n^k u^{(k)}v^{(n-k)}$',
      '罗尔定理：$f$ 在 $[a,b]$ 连续、$(a,b)$ 可导、$f(a)=f(b)$，则存在 $\\xi$ 使 $f\'(\\xi)=0$',
      '拉格朗日中值定理：$f(b)-f(a)=f\'(\\xi)(b-a)$'],
     '会用莱布尼茨公式求高阶导数；罗尔定理证明题能写出前两步'),
    (6, '导数（三）：导数应用与不等式证明', ['5.5', '5.6'],
     ['单调性：$f\'>0$ 则递增，$f\'<0$ 则递减',
      '极值判别：$f\'(x_0)=0$ 且 $f\'\'$ 变号；$f\'\'(x_0)>0$ 为极小，$f\'\'(x_0)<0$ 为极大',
      '水平渐近线：$\\lim_{x\\to\\infty}f(x)=A$ 则 $y=A$；铅直渐近线：$\\lim_{x\\to x_0}f(x)=\\infty$ 则 $x=x_0$'],
     '会用"作差 + 求导 + 判单调"证明简单不等式；会求渐近线'),
    (7, '积分（一）：基本积分表与换元积分', ['6.1', '6.2'],
     ['$\\int x^{\\alpha}dx=\\frac{x^{\\alpha+1}}{\\alpha+1}+C$，$\\int\\frac{dx}{x}=\\ln|x|+C$，$\\int e^xdx=e^x+C$',
      '$\\int\\frac{dx}{1+x^2}=\\arctan x+C$，$\\int\\frac{dx}{\\sqrt{1-x^2}}=\\arcsin x+C$',
      '三角代换：含 $\\sqrt{a^2-x^2}$ 令 $x=a\\sin t$；含 $\\sqrt{x^2+a^2}$ 令 $x=a\\tan t$；含 $\\sqrt{x^2-a^2}$ 令 $x=a\\sec t$'],
     '基本积分表默写全对；凑微分与三角代换能独立完成'),
    (8, '积分（二）：分部积分与有理函数积分', ['6.3', '6.4'],
     ['分部积分公式：$\\int u\\,dv=uv-\\int v\\,du$（"反对幂指三"，排在前面当 $u$）',
      '$\\int\\ln x\\,dx=x\\ln x-x+C$，$\\int\\arctan x\\,dx=x\\arctan x-\\frac12\\ln(1+x^2)+C$',
      '真分式拆项：$\\frac{1}{x(x+1)}=\\frac1x-\\frac{1}{x+1}$'],
     '分部积分的 $u$ 和 $dv$ 选得对；有理函数会拆项'),
    (9, '积分（三）：定积分性质与变限积分', ['6.5', '6.6'],
     ['牛顿–莱布尼茨公式：$\\int_a^b f(x)dx=F(b)-F(a)$',
      '变限积分求导：$\\frac{d}{dx}\\int_a^{\\varphi(x)}f(t)dt=f(\\varphi(x))\\varphi\'(x)$',
      '对称区间：奇函数积分为 $0$；偶函数积分为 $2\\int_0^a f(x)dx$',
      '$\\int_0^a f(x)dx=\\int_0^a f(a-x)dx$'],
     '变限积分求导公式能正确使用；对称区间与配对技巧会用'),
    (10, '定积分应用：面积、旋转体体积、弧长', ['7.1', '7.2'],
     ['面积：$S=\\int_a^b(\\text{上}-\\text{下})dx$ 或 $S=\\int_c^d(\\text{右}-\\text{左})dy$',
      '绕 $x$ 轴旋转体体积：$V=\\pi\\int_a^b f^2(x)dx$',
      '弧长：$s=\\int_a^b\\sqrt{1+[f\'(x)]^2}\\,dx$'],
     '会画图定限；面积与旋转体体积两类题能独立算完'),
    (11, '多元极值与二重积分（一）：直角坐标', ['9.1', '9.2'],
     ['二元极值判别：$A=f_{xx}$，$B=f_{xy}$，$C=f_{yy}$；$AC-B^2>0$ 时有极值（$A>0$ 极小，$A<0$ 极大）',
      '拉格朗日乘数法：构造 $L=f+\\lambda\\varphi$，令各偏导为 $0$',
      '二重积分（X 型）：$\\iint_D f\\,dxdy=\\int_a^b dx\\int_{y_1(x)}^{y_2(x)}f\\,dy$'],
     '二重积分的"画区域 → 定限 → 计算"三步能独立完成'),
    (12, '二重积分（二）与微分方程（一）', ['9.3', '10.1'],
     ['极坐标：$\\iint_D f\\,dxdy=\\int_{\\alpha}^{\\beta}d\\theta\\int_{r_1(\\theta)}^{r_2(\\theta)}f\\,r\\,dr$',
      '可分离变量方程：$\\frac{dy}{dx}=f(x)g(y)\\Rightarrow\\int\\frac{dy}{g(y)}=\\int f(x)dx$',
      '齐次方程：令 $u=\\frac yx$，则 $y\'=u+xu\'$'],
     '会定极坐标下的 $\\theta$ 与 $r$ 的范围；可分离变量方程会求通解'),
    (13, '微分方程（二）：一阶线性与二阶常系数（最高性价比）', ['10.2', '10.5'],
     ['一阶线性通解：$y=e^{-\\int P dx}\\left(\\int Qe^{\\int P dx}dx+C\\right)$',
      '二阶常系数齐次：特征方程 $r^2+pr+q=0$；两个不等实根、重根、共轭复根三种情形',
      '非齐次特解 $y^*$：自由项为 $e^{\\lambda x}P_m(x)$ 时设 $y^*=x^k e^{\\lambda x}Q_m(x)$'],
     '这两节是全资料性价比最高的：微分方程是解答题送分位，必须拿满分'),
    (14, '多元微分（一）：偏导、全微分与链式法则', ['8.1', '8.2'],
     ['全微分：$dz=\\frac{\\partial z}{\\partial x}dx+\\frac{\\partial z}{\\partial y}dy$',
      '链式法则：$z=f(u,v)$，$\\frac{\\partial z}{\\partial x}=\\frac{\\partial f}{\\partial u}\\frac{\\partial u}{\\partial x}+\\frac{\\partial f}{\\partial v}\\frac{\\partial v}{\\partial x}$',
      '可微的必要条件：偏导数存在；充分条件：偏导数连续'],
     '链式法则的"链式图"画得出来；二阶混合偏导会算'),
    (15, '多元微分（二）：隐函数与切平面', ['8.3', '8.4'],
     ['隐函数（一个方程）：$\\frac{\\partial z}{\\partial x}=-\\frac{F_x}{F_z}$，$\\frac{\\partial z}{\\partial y}=-\\frac{F_y}{F_z}$',
      '曲面 $F(x,y,z)=0$ 的切平面：$F_x(x-x_0)+F_y(y-y_0)+F_z(z-z_0)=0$',
      '空间曲线 $x=x(t),y=y(t),z=z(t)$ 的切线方向向量：$(x\'(t_0),y\'(t_0),z\'(t_0))$'],
     '隐函数求导公式记牢；切平面与切线方程会写'),
    (16, '级数（一）与混合限时训练卷 A', ['11.1', '11.2'],
     ['级数收敛的必要条件：通项趋于 $0$',
      '比值判别法：$\\lim\\left|\\frac{a_{n+1}}{a_n}\\right|=\\rho$，$\\rho<1$ 收敛、$\\rho>1$ 发散',
      '$p$ 级数 $\\sum\\frac{1}{n^p}$：$p>1$ 收敛，$p\\le 1$ 发散；几何级数 $\\sum aq^n$：$|q|<1$ 收敛',
      '收敛半径：$R=\\lim\\left|\\frac{a_n}{a_{n+1}}\\right|$'],
     '级数判敛会选判别法；收敛半径会算。今天同时完成混合限时训练卷 A'),
]

PLAN_FOR_MIXED = [
    ('A', 60, [('4.1', 2), ('4.3', 1), ('5.1', 1), ('5.2', 1), ('6.1', 1),
               ('6.3', 1), ('6.5', 1), ('6.6', 1), ('7.1', 1), ('10.1', 1)]),
    ('B', 70, [('6.2', 1), ('6.4', 1), ('7.4', 1), ('9.1', 1), ('9.2', 2),
               ('9.3', 1), ('10.2', 1), ('10.5', 1), ('8.1', 1), ('8.3', 1)]),
    ('C', 80, [('4.4', 1), ('5.4', 1), ('5.5', 1), ('8.2', 1), ('8.4', 1),
               ('9.4', 1), ('10.4', 1), ('11.1', 2), ('11.2', 1), ('12.1', 1)]),
]

EXTRA_SECTIONS = ['7.3', '7.4', '8.5', '9.5', '10.3', '10.6', '11.3', '11.4',
                  '11.5', '12.2', '12.4', '12.5']


def load():
    sections = {}
    chapters = {}
    for name in FILES:
        path = os.path.join(CONTENT, name)
        if not os.path.exists(path):
            print('  !! 缺少 %s' % name)
            continue
        ch = parse_file(path)
        chapters.setdefault(ch.title, [])
        for sec in ch.sections:
            sections[sec.num] = sec
    return sections


def flat(text):
    return re.sub(r'\s*\n\s*', ' ', text).strip()


def sort_problems(sec):
    return sorted(sec.problems, key=lambda p: TYPE_ORDER.get(p.type, 9))


def main():
    sections = load()
    os.makedirs(MY, exist_ok=True)
    total_all = sum(len(s.problems) for s in sections.values())
    used_ids = set()

    # ---------------------------------------------------------- 第二章
    out = []
    out.append('# 第二章　20 天冲刺路线与每日计划')
    out.append('')
    out.append('## 一、三个阶段与总览')
    out.append('')
    out.append('| 阶段 | 天数 | 干什么 | 目标 |')
    out.append('|---|---|---|---|')
    out.append('| 基础抢救 | Day 1–6 | 极限、导数、中值定理，把忘掉的公式捡回来 | '
               '填空第 1 题必拿 |')
    out.append('| 高频专项突破 | Day 7–15 | 积分、二重积分、微分方程、多元微分，按题型刷 | '
               '解答题 2 道必拿 |')
    out.append('| 混合与模拟 | Day 16–20 | 限时训练、3 套模拟卷、错题二刷 | 稳定 40–50 分 |')
    out.append('')
    out.append('**每天固定流程**：① 先读当天题型的"这一类题我到底应该记住什么"；'
               '② 默写当天"必须记住的公式"；③ 限时做题（填空 3–6 分钟/题，解答 8–15 分钟/题）；'
               '④ 对解析，重点看【题型识别】与【易错点】；⑤ 错题录入第十八章模板。')
    out.append('')
    out.append('## 二、每日计划表')
    out.append('')
    out.append('| Day | 学习知识点 | 必做题目 | 加练 | 今日目标 |')
    out.append('|---|---|---|---|---|')

    day_detail = []
    for day, title, secs, formulas, goal in DAYS:
        must, extra = [], []
        for sn in secs:
            sec = sections.get(sn)
            if not sec:
                continue
            for p in sort_problems(sec):
                if len(must) < 13:
                    must.append(p)
                else:
                    extra.append(p)
        for p in must:
            used_ids.add(p.id)
        for p in extra:
            used_ids.add(p.id)
        mrange = '、'.join(p.id for p in must)
        erange = '、'.join(p.id for p in extra) if extra else '—'
        out.append('| Day %d | %s | %s | %s | %s |' % (day, title, mrange, erange, goal))
        day_detail.append((day, title, secs, formulas, goal, must, extra))
    out.append('')
    out.append('> 表中"必做题目"给的是题号，直接翻到对应章节做即可。'
               '加练题只在当天任务提前完成、或学有余力时再做。')
    out.append('')

    out.append('## 三、每日详细任务（Day 1 – Day 16）')
    out.append('')
    for day, title, secs, formulas, goal, must, extra in day_detail:
        mins = sum(int(re.sub(r'\D', '', p.time) or 6) for p in must)
        out.append('### Day %d　%s' % (day, title))
        out.append('')
        out.append('**学习知识点**：' + '；'.join(
            '%s（%s）' % (sections[s].full_title, '、'.join(sorted(set(
                p.kp for p in sections[s].problems))))
            for s in secs if s in sections))
        out.append('')
        out.append('**必须记住的公式**：')
        out.append('')
        for i, f in enumerate(formulas, 1):
            out.append('%d. %s' % (i, f))
        out.append('')
        out.append('**今日母题与基础训练（必做 %d 题，建议总用时约 %d 分钟）**：%s'
                   % (len(must), mins, '、'.join(p.id for p in must)))
        out.append('')
        if extra:
            out.append('**今日加练（选做）**：%s' % '、'.join(p.id for p in extra))
            out.append('')
        out.append('**今日目标分值能力**：%s' % goal)
        out.append('')
        out.append('**今日错题复盘**：把做错或超时的题按第十八章模板记录，'
                   '并写下"我下次看到什么特征该想到这个方法"。')
        out.append('')
    out.append('## 四、模拟与冲刺阶段（Day 17 – Day 20）')
    out.append('')
    out.append('| Day | 任务 | 具体要求 | 目标 |')
    out.append('|---|---|---|---|')
    out.append('| Day 17 | **模拟卷（一）**，严格限时 150 分钟 | '
               '按第十七章时间表执行；做完先只对答案速查，标出错误题号，第二天再细读解析 | '
               '40 分以上 |')
    out.append('| Day 18 | **模拟卷（二）** + 模拟卷一错题细读 | '
               '同样限时 150 分钟；下午把卷一的详细解析逐题读完 | 42 分以上 |')
    out.append('| Day 19 | **模拟卷（三）** + 错题二刷 + 第十二章送分模块（12.1 平面直线、12.3 格林公式） | '
               '模拟卷限时；错题二刷只做之前做错和超时的题 | 45 分以上 |')
    out.append('| Day 20 | **考前总复习**：默写全部公式 + 重读第十七章策略 + 错题三刷 | '
               '不做新题；把"保底 40 分清单"抄写一遍 | 稳定 45–50 分 |')
    out.append('')
    out.append('## 五、选做（加练）模块清单：学有余力再做')
    out.append('')
    out.append('下面这些题型**不影响 40–50 分目标**，只有在当天必做题全部完成、'
               '且时间还有富余时才做。**千万不要为了做它们而跳过必做题。**')
    out.append('')
    out.append('| 题型 | 内容 | 建议 |')
    out.append('|---|---|---|')
    labels = {
        '7.3': '积分不等式与积分中值定理', '7.4': '定积分与数列极限（黎曼和）',
        '8.5': '方向导数与梯度', '9.5': '三重积分基础',
        '10.3': '全微分方程', '10.6': '微分方程应用与综合',
        '11.3': '幂级数求和函数', '11.4': '函数展开成幂级数',
        '11.5': '傅里叶级数基础', '12.2': '常见曲面与投影',
        '12.3': '格林公式基础', '12.4': '数列与级数综合',
        '12.5': '微积分综合题',
    }
    advice = {
        '7.3': 'Day 19 有余力再看', '7.4': '会化黎曼和就能拿分，值得看',
        '8.5': '套公式题，10 分钟就能学会', '9.5': '战略性放弃，只记柱面坐标公式',
        '10.3': '考得少，可跳过', '10.6': '应用题可看一眼',
        '11.3': '难度偏高，选做', '11.4': '记住 5 个常见展开式即可',
        '11.5': '只记狄利克雷收敛定理，选做', '12.2': '选做',
        '12.3': 'Day 19 必看，格林公式性价比高', '12.4': '选做',
        '12.5': '选做',
    }
    for sn in EXTRA_SECTIONS:
        sec = sections.get(sn)
        if not sec:
            continue
        ids = '、'.join(p.id for p in sec.problems)
        out.append('| %s | %s（%d 题：%s） | %s |'
                   % (sec.full_title, labels.get(sn, ''), len(sec.problems), ids,
                      advice.get(sn, '选做')))
    out.append('')

    with open(os.path.join(MY, 'ch02_plan.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))

    # ---------------------------------------------------------- 第十三章
    out = []
    out.append('# 第十三章　混合限时训练（Day 16 使用）')
    out.append('')
    out.append('## 一、这一章怎么用（非常重要）')
    out.append('')
    out.append('前三周你是"按题型"做题的，所以你能猜到用哪个方法。'
               '**考场上没有人告诉你题型。**这一章的任务，就是把题型打乱，'
               '训练你"看到题目 → 判断题型 → 选方法"的条件反射。')
    out.append('')
    out.append('- **做题规则**：不翻前面的章节，看到题先在草稿纸上写下'
               '"这题属于什么题型、该用什么方法"，再动手算。')
    out.append('- **对答案规则**：做完一整卷再对。'
               '每道题的详细解析在对应章节，按"答案索引"里的题号翻回去看。')
    out.append('- **记录规则**：把每道题"你判断的题型"写在下面的"题型判断记录表"里，'
               '再和索引里的真实题型对照。判断错的题，比算错的题更值得记录。')
    out.append('')

    papers = []
    for tag, minutes, picks in PLAN_FOR_MIXED:
        chosen = []
        for sn, cnt in picks:
            sec = sections.get(sn)
            if not sec:
                continue
            ps = sort_problems(sec)
            for p in ps:
                if len([c for c in chosen if c.kp == p.kp]) >= cnt:
                    break
                if p not in chosen:
                    chosen.append(p)
                    if len([c for c in chosen if c.kp == p.kp]) >= cnt:
                        break
        papers.append((tag, minutes, chosen))
        used_ids.update(p.id for p in chosen)

    for tag, minutes, chosen in papers:
        out.append('## 二、混合限时训练卷 %s（建议限时 %d 分钟，共 %d 题）'
                   % (tag, minutes, len(chosen)))
        out.append('')
        out.append('> 做题顺序：先通览全卷 3 分钟，给每题标记 A（会做）/ B（知道方向）/ C（没思路），'
                   '然后按 A → B → C 的顺序做。到点立刻停笔。')
        out.append('')
        for i, p in enumerate(chosen, 1):
            out.append('**第 %d 题**（建议用时 %s）' % (i, p.time))
            out.append('')
            out.append(flat(p.fields.get('STEM', '')))
            out.append('')
        out.append('### 题型判断记录表（做完再对索引）')
        out.append('')
        out.append('| 题号 | 我判断的题型 | 我用的方法 | 结果（对/错/超时） | 我该想到的方法 |')
        out.append('|---|---|---|---|---|')
        for i in range(1, len(chosen) + 1):
            out.append('| 第 %d 题 |  |  |  |  |' % i)
        out.append('')
        out.append('### 答案索引（先做完再看）')
        out.append('')
        out.append('| 题号 | 答案 | 真实题型 | 详细解析位置 |')
        out.append('|---|---|---|---|')
        for i, p in enumerate(chosen, 1):
            out.append('| 第 %d 题 | %s | %s | 题 %s |'
                       % (i, flat(p.fields.get('ANSWER', '')), p.kp, p.id))
        out.append('')

    with open(os.path.join(MY, 'ch13_mixed.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))

    # ---------------------------------------------------------- 附录
    out = []
    out.append('# 附录 A　20 天打卡表（打印后手写）')
    out.append('')
    out.append('每天完成后打勾。**连续两天没完成，就把当天的加练全部删掉，只保必做。**')
    out.append('')
    out.append('| Day | 当天任务 | 计划用时 | 实际用时 | 完成 | 错题数 | 二刷日期 |')
    out.append('|---|---|---|---|---|---|---|')
    for day, title, secs, formulas, goal in DAYS:
        out.append('| Day %d | %s | 150 分钟 |  | □ |  |  |' % (day, title))
    out.append('| Day 17 | 模拟卷（一）限时 150 分钟 + 对答案 | 180 分钟 |  | □ |  |  |')
    out.append('| Day 18 | 模拟卷（二）+ 卷一错题细读 | 180 分钟 |  | □ |  |  |')
    out.append('| Day 19 | 模拟卷（三）+ 错题二刷 + 12.1/12.3 | 180 分钟 |  | □ |  |  |')
    out.append('| Day 20 | 总复习：公式默写 + 策略 + 错题三刷 | 150 分钟 |  | □ |  |  |')
    out.append('')
    out.append('# 附录 B　考前 3 天与考试当天清单')
    out.append('')
    out.append('## 一、考前 3 天（对应 Day 18–20）')
    out.append('')
    out.append('- [ ] 不再做新题，只做错题本里的题和模拟卷错题。')
    out.append('- [ ] 把第三章"必背基础公式手册"完整默写一遍，错的公式单独抄 5 遍。')
    out.append('- [ ] 把第十七章"保底 40 分清单"（13 条）默写一遍。')
    out.append('- [ ] 用第十七章的时间表完整走一遍流程（哪怕只做半套卷）。')
    out.append('- [ ] 提前把计算器、准考证、身份证、笔、橡皮放进包里（按赛区要求，'
               '多数赛区不允许使用计算器，以准考证说明为准）。')
    out.append('')
    out.append('## 二、考试当天')
    out.append('')
    out.append('- [ ] 8:00 前到考场，进考场前**只看"保底 40 分清单"那一页**，不做新题。')
    out.append('- [ ] 9:00 开考后先花 5 分钟通览全卷，给 10 道题贴 A / B / C 标签。')
    out.append('- [ ] 填空题 45 分钟内必须全部结束（每题 ≤ 6 分钟）。')
    out.append('- [ ] 解答题先做微分方程，再做二重积分/面积体积。')
    out.append('- [ ] 每题开头写"解："或"证明："，公式单独成行。')
    out.append('- [ ] 最后 10 分钟按第十七章检查清单逐项打勾。')
    out.append('')
    out.append('# 附录 C　最容易丢分的 18 个计算细节（考前速查）')
    out.append('')
    out.append('| 序号 | 细节 | 正确做法 |')
    out.append('|---|---|---|')
    details = [
        ('负号', '$(x-1)(x-2)(x-3)$ 在 $x=0$ 处是 $(-1)(-2)(-3)$，三个负号得 $-6$，'
                 '不是 $+6$', '先数负号个数'),
        ('约分', '约掉公因子前必须说明 $x\\neq 0$（求极限时 $x\\to 0$ 但 $x\\neq 0$）',
         '写一句"因 $x\\neq 0$，可约"'),
        ('洛必达', '只有 $\\frac00$ 或 $\\frac\\infty\\infty$ 型才能用洛必达',
         '用之前先写"这是 $\\frac00$ 型"'),
        ('等价无穷小', '只能在乘除因子中替换，加减中不能替换',
         '遇到加减结构改用泰勒展开'),
        ('不定积分常数', '不定积分结果必须带 $+C$', '写完立刻检查 $+C$'),
        ('绝对值', '$\\int\\frac{dx}{x}=\\ln|x|+C$，不要丢绝对值', '记成 $\\ln|x|$'),
        ('上下限', '牛顿–莱布尼茨是"上限代入减下限代入"', '写清 $F(b)-F(a)$'),
        ('代换上下限', '定积分换元后上下限必须一起换，最后不需要换回 $x$',
         '换元后立刻改上下限'),
        ('参数方程二阶导', '$\\frac{d^2y}{dx^2}=\\frac{d}{dt}(y\'/x\')\\div x\'(t)$，'
                           '别忘了除以 $x\'(t)$', '写公式再代数'),
        ('隐函数求导', '对 $y$ 求导时要乘 $y\'$', '每出现一次 $y$ 就乘一个 $y\'$'),
        ('链式法则', '抽象函数 $f(u,v)$ 求二阶导时，$f_u$ 仍是 $u,v$ 的函数，'
                     '还要再求一次导', '画链式图再算'),
        ('极值判别', '$AC-B^2>0$ 才有极值；$AC-B^2<0$ 是鞍点，没有极值',
         '先算 $A,B,C$ 再判'),
        ('二重积分定限', 'X 型区域：先 $dx$ 后 $dy$；定限时内层上下限可以是 $x$ 的函数，'
                         '外层必须是常数', '画图后逐条写不等式'),
        ('极坐标', '别忘了面积元素里的 $r$（$dxdy=r\\,dr\\,d\\theta$）',
         '写 $r$ 再积分'),
        ('特征方程', '二阶常系数方程写特征方程 $r^2+pr+q=0$，'
                     '重根时通解要写 $C_1e^{rx}+C_2xe^{rx}$', '三种情形背下来'),
        ('级数必要性', '通项不趋于 $0$ 一定发散；但通项趋于 $0$ 不代表收敛',
         '先看通项再选判别法'),
        ('收敛半径', '$R=\\lim|a_n/a_{n+1}|$，不要写反成 $|a_{n+1}/a_n|$',
         '记清分母是 $a_{n+1}$'),
        ('写步骤分', '不会做也要写：题设条件 + 所用定理 + 前两步 + 结论形式',
         '绝不写"显然"'),
    ]
    for i, (a, b, c) in enumerate(details, 1):
        out.append('| %d | %s | %s |' % (i, a, c))
    out.append('')
    out.append('> 这 18 条是"会做却做错"的全部来源。**考前把这一页读三遍，'
               '比你多做 20 道题更值。**')
    out.append('')

    with open(os.path.join(MY, 'appendix.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))

    # ---------------------------------------------------------- 统计
    print('题库总题数：%d' % total_all)
    must_total = 0
    for day, title, secs, formulas, goal in DAYS:
        n = 0
        for sn in secs:
            sec = sections.get(sn)
            if sec:
                n += min(13, len(sec.problems))
        must_total += n
    print('Day1-16 必做题数：约 %d' % must_total)
    print('已生成：ch02_plan.txt / ch13_mixed.txt / appendix.txt')
    missing = [s for s in EXTRA_SECTIONS if s not in sections]
    if missing:
        print('注意：以下选做题型尚未生成：%s' % '、'.join(missing))


if __name__ == '__main__':
    main()