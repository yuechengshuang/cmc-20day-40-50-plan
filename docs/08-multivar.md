# 第八章　多元函数微分学

## 本章拿分指南
> 本章共 **28** 题。


本章在 CMC 非数学类初赛里的地位：多元函数微分学是初赛的高频板块，填空题里经常考"求某点处的偏导数""求全微分 $dz$""判断在原点是否可微"，解答题里则以"隐函数求偏导""复合函数求导"的形式出现。这一章的特点是公式链条短、套路极其固定：只要把链式法则的"链式图"画对、把每一层该乘的因子都乘上，绝大多数题都能在五分钟内算出结果，是基础薄弱学生最值得优先攻克的计算板块之一。

从 20 分提高到 40 分，本章至少要保证 6 到 10 分的稳定收入。复习时按下面的顺序优先：

- 第一优先：偏导数的直接计算。方法只有一句话，求 $\frac{\partial z}{\partial x}$ 时把 $y$ 当成一个常数，按一元函数求导法则求导；求 $\frac{\partial z}{\partial y}$ 时把 $x$ 当成常数。用到哪条一元法则（乘积、商、复合）就先在草稿纸上写清是哪一条，再动手算。
- 第二优先：全微分公式。$dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy$，所以"求 $dz$"这道题本质上是"求两个一阶偏导"，算完偏导代入即可，不要另记新公式。
- 第三优先：可微性判定。在原点这类特殊点，偏导往往要用定义算：$f_x(0,0)=\lim_{x\to 0}\frac{f(x,0)-f(0,0)}{x}$。判定可微必须验证 $\lim_{(x,y)\to(0,0)}\frac{f(x,y)-f(0,0)-f_x(0,0)x-f_y(0,0)y}{\sqrt{x^2+y^2}}=0$，这一步只能按定义做，不能用"偏导连续"来代替，因为偏导连续只是可微的充分条件。
- 第四优先：复合函数与隐函数的链式法则。复合函数求导的关键是画链式图：先写出所有中间变量（例如 $u$、$v$），再看从 $z$ 到 $x$ 一共有几条路径，有几条路径就有几项，每一项是"沿这条路径每一段的导数连乘"。隐函数求导的关键是记住一元公式 $\frac{dy}{dx}=-\frac{F_x}{F_y}$ 的多元版本 $\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}$，其中 $F(x,y,z)=0$，求 $F_z$ 时把 $x$、$y$ 都当常数。

本章学习方法的建议：每道题先在草稿纸上写出所有中间变量和链式图，再把每一项乘出来，最后才代入数字。丢分往往不是不会求导，而是"少乘了一个因子"或者"把 $f_1'$ 和 $f_2'$ 的位置写反"。所有涉及二阶偏导的题，算完以后务必用一次交换求导次序的结果互相校对，两次结果应当一致。

## 8.1 题型一 偏导数、全微分与可微性判定

> **这一类题我到底应该记住什么？**
>
> 这一类题的三个基本动作：一是"求偏导就把另一个变量当常数"，求 $\frac{\partial z}{\partial x}$ 时视 $y$ 为常数，按一元函数求导法则算，求 $\frac{\partial z}{\partial y}$ 时视 $x$ 为常数。
> 二是"求全微分就等于求两个一阶偏导"，先算出 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$，再写成 $dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy$，不要另发明公式。
> 三是在原点这类特殊点求偏导或判断可微，一律回到定义：$f_x(0,0)$ 用一元差商极限算，判断可微则必须验证差商式 $\frac{f(x,y)-f(0,0)-f_x(0,0)x-f_y(0,0)y}{\sqrt{x^2+y^2}}$ 的极限为零。
> 求二阶混合偏导时先求一阶偏导，再把已经求出的偏导函数对另一个变量再求一次导；算完后可以换一个次序再求一次，两次结果一样才对。

### 题 8.1-1　【母题】　难度 ★　建议用时 6分钟　重要程度 ★★★★★

**知识点**：多元微分/偏导数

**【题目】**

设 $z=x^3y+xy^2$，求 $\frac{\partial z}{\partial x}$、$\frac{\partial z}{\partial y}$，并求在点 $(1,2)$ 处的值 $\frac{\partial z}{\partial x}\big|_{(1,2)}$ 与 $\frac{\partial z}{\partial y}\big|_{(1,2)}$。（根据 CMC 常见题型改编）

**【考查知识点】**

多项式函数的偏导数：求 $\frac{\partial z}{\partial x}$ 时把 $y$ 看成常数，求 $\frac{\partial z}{\partial y}$ 时把 $x$ 看成常数。

**【题型识别】**

题型识别：看到"给出一个显式的二元初等函数，要求偏导函数或某点处的偏导数值"这个特征 → 属于偏导数直接计算的最基本题型 → 用"对一个变量求导、把另一个变量当常数"的方法，套用一元函数的乘积求导法则。

**【需要记住的公式】**

1. 偏导数记号：$z=f(x,y)$ 时 $f_x(x,y)=\frac{\partial f}{\partial x}$
2. 幂函数求导：$(x^n)'=nx^{n-1}$
3. 乘积求导法则：$(uv)'=u'v+uv'$

**【解题思路】**

解题思路：这个函数是 $x$、$y$ 的多项式，$x^3y$ 是 $x^3$ 与 $y$ 的乘积，$xy^2$ 是 $x$ 与 $y^2$ 的乘积。求 $\frac{\partial z}{\partial x}$ 时把 $y$ 当作一个普通的常数，于是 $x^3y$ 对 $x$ 求导得 $3x^2y$（常数 $y$ 原样保留），$xy^2$ 对 $x$ 求导得 $y^2$。求 $\frac{\partial z}{\partial y}$ 时把 $x$ 当作常数，$x^3y$ 对 $y$ 求导得 $x^3$，$xy^2$ 对 $y$ 求导得 $2xy$。最后把 $x=1$、$y=2$ 分别代入两个偏导函数即可。

**【详细解答】**

第一步：求 $\frac{\partial z}{\partial x}$。把 $y$ 看成常数，逐项对 $x$ 求导：

第一项 $x^3y$：$x^3$ 对 $x$ 求导等于 $3x^2$，常数因子 $y$ 不动，所以这一项求导得 $3x^2y$。

第二项 $xy^2$：$x$ 对 $x$ 求导等于 $1$，$y^2$ 作为常数因子不动，所以这一项求导得 $y^2$。

相加得
$$\frac{\partial z}{\partial x}=3x^2y+y^2$$

第二步：求 $\frac{\partial z}{\partial y}$。把 $x$ 看成常数，逐项对 $y$ 求导：

第一项 $x^3y$：$y$ 对 $y$ 求导等于 $1$，$x^3$ 作为常数因子不动，所以这一项求导得 $x^3$。

第二项 $xy^2$：$y^2$ 对 $y$ 求导等于 $2y$，$x$ 作为常数因子不动，所以这一项求导得 $2xy$。

相加得
$$\frac{\partial z}{\partial y}=x^3+2xy$$

第三步：代入点 $(1,2)$。在 $\frac{\partial z}{\partial x}=3x^2y+y^2$ 中令 $x=1$、$y=2$：
$$\frac{\partial z}{\partial x}\bigg|_{(1,2)}=3\cdot 1^2\cdot 2+2^2=6+4=10$$

在 $\frac{\partial z}{\partial y}=x^3+2xy$ 中令 $x=1$、$y=2$：
$$\frac{\partial z}{\partial y}\bigg|_{(1,2)}=1^3+2\cdot 1\cdot 2=1+4=5$$

第四步：验算。用定义直接算 $x$ 方向的偏导数值。固定 $y=2$，这时 $z=x^3\cdot 2+x\cdot 4=2x^3+4x$，把它看成 $x$ 的一元函数，求导得 $6x^2+4$，代入 $x=1$ 得 $6+4=10$，与上面结果 10 一致。再固定 $x=1$，这时 $z=y+y^2$，对 $y$ 求导得 $1+2y$，代入 $y=2$ 得 $1+4=5$，与上面结果 5 一致。两个数值都通过验算。

**【最终答案】**

$\frac{\partial z}{\partial x}=3x^2y+y^2$，$\frac{\partial z}{\partial y}=x^3+2xy$；$\frac{\partial z}{\partial x}\big|_{(1,2)}=10$，$\frac{\partial z}{\partial y}\big|_{(1,2)}=5$

**【易错点】**

最常见的错误是求 $\frac{\partial z}{\partial x}$ 时把 $y$ 也当成变量对 $x$ 求导，写出 $3x^2y+xy'$ 这类没有意义的式子。要牢记：求偏导时另一个变量是常数，它的导数是 0，它本身按常数因子原样保留。第二个错误是代入数值时把两个偏导函数搞混，建议先把两个偏导函数分别写清楚再代入。

**【同类题识别技巧】**

以后看到"显式二元函数求偏导"，先在心里说一句"对 $x$ 求导，$y$ 是常数"，再逐项套一元求导法则。凡是被积函数或函数式中含乘积因子的，都要检查是否用到乘积求导法则。

**【一句话总结】**

看到显式二元函数求偏导 → 求谁把另一个变量当常数，逐项套一元求导法则。

### 题 8.1-2　【变式】　难度 ★★　建议用时 7分钟　重要程度 ★★★★★

**知识点**：多元微分/全微分

**【题目】**

设 $z=e^{x}\sin y+x^2y$，求全微分 $dz$。（专项训练原创题）

**【考查知识点】**

全微分公式 $dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy$ 的应用，关键是先算两个一阶偏导。

**【题型识别】**

题型识别：看到"求全微分 $dz$"这个特征 → 属于全微分的直接计算题型 → 用"先求 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$，再套 $dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy$"的方法，不要另记新公式。

**【需要记住的公式】**

1. 全微分公式：$dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy$
2. 指数函数求导：$(e^x)'=e^x$
3. 三角函数求导：$(\sin y)'=\cos y$，$(\cos y)'=-\sin y$

**【解题思路】**

解题思路：全微分这道题本质上是一道"求两个一阶偏导"的题。函数由两部分相加：$e^x\sin y$ 与 $x^2y$。求 $\frac{\partial z}{\partial x}$ 时把 $y$ 当常数，$e^x$ 求导是 $e^x$，$\sin y$ 作为常数因子不动，得 $e^x\sin y$；$x^2y$ 对 $x$ 求导得 $2xy$。求 $\frac{\partial z}{\partial y}$ 时把 $x$ 当常数，$e^x$ 作为常数因子不动，$\sin y$ 求导是 $\cos y$，得 $e^x\cos y$；$x^2y$ 对 $y$ 求导得 $x^2$。两个偏导都算好后直接代入全微分公式。

**【详细解答】**

第一步：求 $\frac{\partial z}{\partial x}$。把 $y$ 看成常数。

对 $e^x\sin y$ 求关于 $x$ 的偏导：$\sin y$ 是常数因子，$e^x$ 对 $x$ 求导仍为 $e^x$，所以得到 $e^x\sin y$。

对 $x^2y$ 求关于 $x$ 的偏导：$y$ 是常数因子，$x^2$ 对 $x$ 求导得 $2x$，所以得到 $2xy$。

两式相加：
$$\frac{\partial z}{\partial x}=e^x\sin y+2xy$$

第二步：求 $\frac{\partial z}{\partial y}$。把 $x$ 看成常数。

对 $e^x\sin y$ 求关于 $y$ 的偏导：$e^x$ 是常数因子，$\sin y$ 对 $y$ 求导得 $\cos y$，所以得到 $e^x\cos y$。

对 $x^2y$ 求关于 $y$ 的偏导：$x^2$ 是常数因子，$y$ 对 $y$ 求导得 $1$，所以得到 $x^2$。

两式相加：
$$\frac{\partial z}{\partial y}=e^x\cos y+x^2$$

第三步：写出全微分。
$$dz=(e^x\sin y+2xy)\,dx+(e^x\cos y+x^2)\,dy$$

第四步：验算。取点 $(0,0)$ 代入两个偏导函数，得到 $\frac{\partial z}{\partial x}\big|_{(0,0)}=e^0\cdot\sin 0+2\cdot 0\cdot 0=0$，$\frac{\partial z}{\partial y}\big|_{(0,0)}=e^0\cdot\cos 0+0^2=1$。再直接用函数值检查：$z(0,0)=e^0\sin 0+0=0$，$z(0.001,0)=e^{0.001}\sin 0+0=0$，所以沿 $x$ 方向函数值在原点附近几乎不变，与 $z_x(0,0)=0$ 相符；$z(0,0.001)=1\cdot\sin 0.001+0\approx 0.001$，函数值的变化量与 $\Delta y=0.001$ 之比约为 $1$，与 $z_y(0,0)=1$ 相符。两个偏导数值都通过验算。

**【最终答案】**

$dz=(e^x\sin y+2xy)\,dx+(e^x\cos y+x^2)\,dy$

**【易错点】**

常见错误有三处：一是求 $\frac{\partial z}{\partial x}$ 时把 $\sin y$ 也求了导，写成了 $e^x\cos y$，这是把"对 $x$ 求偏导"做成了"对 $y$ 求偏导"；二是最后忘记把 $dx$ 和 $dy$ 写全，只写两个系数；三是把 $e^x\cos y$ 的常数因子 $e^x$ 丢掉。全微分是一个微分表达式，$dx$、$dy$ 是它的组成部分，不能省略。

**【同类题识别技巧】**

以后看到"求 $dz$"或"求全微分"，先默写一遍 $dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy$，然后老老实实算两个偏导，最后把 $dx$、$dy$ 乘上去。全微分还可以用来做近似计算：$f(x_0+\Delta x,y_0+\Delta y)\approx f(x_0,y_0)+\frac{\partial z}{\partial x}\Delta x+\frac{\partial z}{\partial y}\Delta y$。

**【一句话总结】**

看到求全微分 $dz$ → 先算两个一阶偏导，再乘上 $dx$、$dy$ 相加。

### 题 8.1-3　【变式】　难度 ★★　建议用时 10分钟　重要程度 ★★★★★

**知识点**：多元微分/可微性

**【题目】**

设
$$f(x,y)=\begin{cases} \frac{xy}{\sqrt{x^2+y^2}}, & (x,y)\neq (0,0) \\ 0, & (x,y)=(0,0) \end{cases}$$
用定义判断 $f$ 在原点 $(0,0)$ 处是否可微。（根据 CMC 常见题型改编）

**【考查知识点】**

用定义计算原点处的两个偏导数，再按定义验证全增量与全微分之差是否为 $\sqrt{x^2+y^2}$ 的高阶无穷小。

**【题型识别】**

题型识别：看到"分段函数，在原点处判断是否可微"这个特征 → 属于可微性判定的定义法题型 → 用"先用定义算 $f_x(0,0)$ 与 $f_y(0,0)$，再验证 $\lim_{(x,y)\to(0,0)}\frac{\Delta z-f_x(0,0)x-f_y(0,0)y}{\sqrt{x^2+y^2}}=0$"的方法。

**【需要记住的公式】**

1. 偏导数定义：$f_x(0,0)=\lim_{x\to 0}\frac{f(x,0)-f(0,0)}{x}$
2. 可微定义：$\Delta z-f_x(0,0)\Delta x-f_y(0,0)\Delta y=o\left(\sqrt{\Delta x^2+\Delta y^2}\right)$
3. 有界量与无穷小之积仍是无穷小：$\left|\frac{x}{\sqrt{x^2+y^2}}\right|\leq 1$

**【解题思路】**

解题思路：原点处的偏导数不能把 $f$ 的表达式直接求导代入，因为分段函数在原点两侧的表达式不同，必须回到差商定义。要注意在 $y=0$ 这条直线上（原点除外）$f(x,0)=\frac{x\cdot 0}{\sqrt{x^2+0}}=0$，在 $x=0$ 这条直线上（原点除外）$f(0,y)=0$，所以两个差商都恒等于 0，两个偏导都是 0。接下来按定义验证可微性：全增量 $\Delta z=f(x,y)-f(0,0)=\frac{xy}{\sqrt{x^2+y^2}}$，全微分是 $0\cdot x+0\cdot y=0$，所以要检验的量就是 $\frac{xy}{\sqrt{x^2+y^2}}$ 除以 $\sqrt{x^2+y^2}$，即 $\frac{xy}{x^2+y^2}$。用极坐标 $x=t\cos\theta$、$y=t\sin\theta$ 代入，这个式子化为 $\frac{t^2\cos\theta\sin\theta}{t^2}=\cos\theta\sin\theta$，它沿不同方向取不同的值，所以极限不存在，函数不可微。注意：如果改用 $\frac{|xy|^{3/2}}{\sqrt{x^2+y^2}}$ 这类结构，把检验式 $\frac{f(x,y)}{\sqrt{x^2+y^2}}$ 用极坐标代换后得到 $t\cos^{3/2}\theta\sin^{3/2}\theta\to 0$，那时函数就是可微的，区别就在于极坐标代换后的检验式是否含有 $t$ 的正幂次。

**【详细解答】**

第一步：用定义求 $f_x(0,0)$。这里 $\Delta x=x$，而 $f(x,0)$ 需要分两种情况：当 $x\neq 0$ 时，点 $(x,0)$ 不在原点，用第一个表达式
$$f(x,0)=\frac{x\cdot 0}{\sqrt{x^2+0^2}}=\frac{0}{|x|}=0$$
当 $x=0$ 时 $f(0,0)=0$。所以差商为
$$\frac{f(x,0)-f(0,0)}{x}=\frac{0-0}{x}=0\quad(x\neq 0)$$
因此
$$f_x(0,0)=\lim_{x\to 0}\frac{f(x,0)-f(0,0)}{x}=\lim_{x\to 0}0=0$$

第二步：用定义求 $f_y(0,0)$。同样地，当 $y\neq 0$ 时
$$f(0,y)=\frac{0\cdot y}{\sqrt{0^2+y^2}}=\frac{0}{|y|}=0$$
所以
$$f_y(0,0)=\lim_{y\to 0}\frac{f(0,y)-f(0,0)}{y}=\lim_{y\to 0}\frac{0-0}{y}=0$$

第三步：写出需要验证的表达式。由可微的定义，$f$ 在原点可微等价于下式成立：
$$\lim_{(x,y)\to(0,0)}\frac{f(x,y)-f(0,0)-f_x(0,0)x-f_y(0,0)y}{\sqrt{x^2+y^2}}=0$$
把 $f(0,0)=0$、$f_x(0,0)=0$、$f_y(0,0)=0$ 以及 $(x,y)\neq(0,0)$ 时 $f(x,y)=\frac{xy}{\sqrt{x^2+y^2}}$ 代入，分子就是 $\frac{xy}{\sqrt{x^2+y^2}}-0-0-0$，于是要验证的极限是
$$L=\lim_{(x,y)\to(0,0)}\frac{\frac{xy}{\sqrt{x^2+y^2}}}{\sqrt{x^2+y^2}}=\lim_{(x,y)\to(0,0)}\frac{xy}{x^2+y^2}$$

第四步：用极坐标证明这个极限不存在。令
$$x=t\cos\theta,\qquad y=t\sin\theta\quad(t>0)$$
当 $(x,y)\to(0,0)$ 时有 $t\to 0^{+}$，并且 $x^2+y^2=t^2$，$xy=t^2\cos\theta\sin\theta$。代入得
$$\frac{xy}{x^2+y^2}=\frac{t^2\cos\theta\sin\theta}{t^2}=\cos\theta\sin\theta$$
这个结果与 $t$ 无关，只与方向角 $\theta$ 有关。取 $\theta=\frac{\pi}{4}$（沿直线 $y=x$ 趋近原点）得 $L=\frac{\sqrt{2}}{2}\cdot\frac{\sqrt{2}}{2}=\frac12$；取 $\theta=0$（沿 $x$ 轴趋近原点）得 $L=0$。沿两条不同路径趋近原点得到两个不同的值，所以这个二重极限不存在。

第五步：验算与结论。另外用两条直线直接检验：沿 $y=x$ 时 $f(x,x)=\frac{x^2}{\sqrt{2x^2}}=\frac{|x|}{\sqrt{2}}$，于是 $\frac{f(x,x)}{\sqrt{x^2+x^2}}=\frac{|x|/\sqrt{2}}{\sqrt{2}|x|}=\frac12$；沿 $y=0$ 时 $f(x,0)=0$，于是 $\frac{f(x,0)}{\sqrt{x^2+0}}=0$。两个值不同，与极坐标的结论一致，说明检验式趋于零的要求不满足。因此 $f$ 在原点处不可微（虽然它的两个偏导数都存在）。

**【最终答案】**

$f_x(0,0)=0$，$f_y(0,0)=0$；因为 $\lim_{(x,y)\to(0,0)}\frac{f(x,y)-f_x(0,0)x-f_y(0,0)y}{\sqrt{x^2+y^2}}=\lim_{(x,y)\to(0,0)}\frac{xy}{x^2+y^2}$ 不存在，所以 $f$ 在原点处不可微。

**【易错点】**

第一个坑：直接对 $\frac{xy}{\sqrt{x^2+y^2}}$ 求导再代入原点，这是错的，原点处必须回定义算差商。第二个坑：算出差商后只检验路径 $y=x$ 就下结论"极限不存在"，理由不完整，必须给出两条路径取不同值才算证明极限不存在。第三个坑：把"两个偏导数存在"当成"可微"，两者之间没有蕴含关系，本题恰好是偏导存在但不可微的例子。第四个坑：对 $\sqrt{x^2+y^2}$ 在原点处求导时会遇到分母为零，要意识到这里不能求导只能回定义。

**【同类题识别技巧】**

以后看到"在原点（或其他特殊点）判断可微"，固定四步走：求 $f(0,0)$、用定义求两个偏导、写出差商式、用极坐标代换或两条路径判断极限是否为零。凡是被积表达式在极坐标下化为"只含 $\theta$"的形式，就说明极限不存在；化为"$t$ 的正幂次乘上有界量"的形式，就说明极限为零、函数可微。

**【一句话总结】**

看到原点处判断可微 → 回定义算偏导，再算差商式看它是不是 $\sqrt{x^2+y^2}$ 的高阶无穷小。

### 题 8.1-4　【变式】　难度 ★★　建议用时 7分钟　重要程度 ★★★★★

**知识点**：多元微分/高阶偏导

**【题目】**

设 $z=x^3y^2+2xy$，求二阶混合偏导数 $\frac{\partial^2 z}{\partial x\partial y}$ 与 $\frac{\partial^2 z}{\partial y\partial x}$。（专项训练原创题）

**【考查知识点】**

二阶混合偏导数的计算与"混合偏导相等"的相互验算。

**【题型识别】**

题型识别：看到"求二阶混合偏导 $\frac{\partial^2 z}{\partial x\partial y}$"这个特征 → 属于高阶偏导数的计算题型 → 用"先求一阶偏导，再把已求出的偏导函数对另一个变量再求一次导"的方法，算完用交换次序的结果互相校对。

**【需要记住的公式】**

1. 二阶混合偏导记号：$\frac{\partial^2 z}{\partial x\partial y}=\frac{\partial}{\partial x}\left(\frac{\partial z}{\partial y}\right)$
2. 幂函数求导：$(x^n)'=nx^{n-1}$
3. 混合偏导相等的条件：偏导函数连续时 $\frac{\partial^2 z}{\partial x\partial y}=\frac{\partial^2 z}{\partial y\partial x}$

**【解题思路】**

解题思路：这道题要走两遍链式顺序。第一遍求 $\frac{\partial^2 z}{\partial x\partial y}$：先求 $\frac{\partial z}{\partial y}$（把 $x$ 当常数），再把它对 $x$ 求导（把 $y$ 当常数）。第二遍求 $\frac{\partial^2 z}{\partial y\partial x}$：先求 $\frac{\partial z}{\partial x}$（把 $y$ 当常数），再把它对 $y$ 求导（把 $x$ 当常数）。本题的函数是多项式，各阶偏导函数都连续，所以两个混合偏导必然相等，这正好可以用来互相验算。

**【详细解答】**

第一步：求一阶偏导 $\frac{\partial z}{\partial y}$（把 $x$ 看成常数）。

$x^3y^2$ 对 $y$ 求导：$x^3$ 是常数因子，$y^2$ 求导得 $2y$，所以得 $2x^3y$。

$2xy$ 对 $y$ 求导：$2x$ 是常数因子，$y$ 求导得 $1$，所以得 $2x$。

相加得
$$\frac{\partial z}{\partial y}=2x^3y+2x$$

第二步：求 $\frac{\partial^2 z}{\partial x\partial y}$，即把上一步的结果对 $x$ 求导（把 $y$ 看成常数）。

$2x^3y$ 对 $x$ 求导：$2y$ 是常数因子，$x^3$ 求导得 $3x^2$，所以得 $6x^2y$。

$2x$ 对 $x$ 求导：得 $2$。

相加得
$$\frac{\partial^2 z}{\partial x\partial y}=6x^2y+2$$

第三步：求一阶偏导 $\frac{\partial z}{\partial x}$（把 $y$ 看成常数）。

$x^3y^2$ 对 $x$ 求导：$y^2$ 是常数因子，$x^3$ 求导得 $3x^2$，所以得 $3x^2y^2$。

$2xy$ 对 $x$ 求导：$2y$ 是常数因子，$x$ 求导得 $1$，所以得 $2y$。

相加得
$$\frac{\partial z}{\partial x}=3x^2y^2+2y$$

第四步：求 $\frac{\partial^2 z}{\partial y\partial x}$，即把上一步的结果对 $y$ 求导（把 $x$ 看成常数）。

$3x^2y^2$ 对 $y$ 求导：$3x^2$ 是常数因子，$y^2$ 求导得 $2y$，所以得 $6x^2y$。

$2y$ 对 $y$ 求导：得 $2$。

相加得
$$\frac{\partial^2 z}{\partial y\partial x}=6x^2y+2$$

第五步：验算。用数值微分检查。取点 $(1,1)$，由答案 $\frac{\partial^2 z}{\partial x\partial y}=6x^2y+2$ 得数值 $6+2=8$。现在用差商近似验算：先算 $\frac{\partial z}{\partial y}$ 在 $(1,1)$ 处的值，由第一步的公式得 $2\cdot 1^3\cdot 1+2\cdot 1=4$；在 $(1.001,1)$ 处的值，由公式得 $2\cdot 1.001^3\cdot 1+2\cdot 1.001\approx 2\cdot 1.003003+2.002=2.006006+2.002=4.008006$。二者的差除以 $\Delta x=0.001$ 得 $\frac{4.008006-4}{0.001}\approx 8.006$，与 $8$ 接近。两个混合偏导的结果完全相同，与"偏导连续时混合偏导相等"的结论一致，答案可靠。

**【最终答案】**

$\frac{\partial^2 z}{\partial x\partial y}=6x^2y+2$，$\frac{\partial^2 z}{\partial y\partial x}=6x^2y+2$，两者相等。

**【易错点】**

最容易错的地方是把符号顺序理解反了：$\frac{\partial^2 z}{\partial x\partial y}$ 表示"先对 $y$ 求导、再对 $x$ 求导"，分母中靠右的变量是先求导的那一个。第二个错误是求完一阶偏导后对同一个变量再求一次导，比如把 $\frac{\partial z}{\partial y}$ 再对 $y$ 求导当作 $\frac{\partial^2 z}{\partial x\partial y}$，那就变成了 $\frac{\partial^2 z}{\partial y^2}$。第三个错误是漏掉 $2xy$ 这一项，直接只对 $x^3y^2$ 求二阶偏导。

**【同类题识别技巧】**

以后看到"求两个混合偏导"，就按两条不同路线各走一遍，最后比对结果。只要函数是初等函数且偏导函数连续（本章题目基本都满足），两个结果一定相等；如果算出来不相等，说明中间某一步算错了，回头检查一阶偏导。

**【一句话总结】**

看到求二阶混合偏导 → 先求一阶偏导再对另一个变量求导，两种次序各算一遍互相校对。

### 题 8.1-5　【基础训练】　难度 ★★　建议用时 6分钟　重要程度 ★★★★★

**知识点**：多元微分/可微性

**【题目】**

设
$$f(x,y)=\begin{cases} (x^2+y^2)\sin\frac{1}{x^2+y^2}, & (x,y)\neq (0,0) \\ 0, & (x,y)=(0,0) \end{cases}$$
用定义判断 $f$ 在原点 $(0,0)$ 处是否可微。（专项训练原创题）

**【考查知识点】**

有界振荡因子与无穷小相乘时的可微性判定：极坐标代换后判定极限是否为零。

**【题型识别】**

题型识别：看到"分段函数里含 $\sin\frac{1}{x^2+y^2}$ 这类振荡因子，要判断原点处是否可微"这个特征 → 属于可微性判定的定义法题型 → 用"用定义求两个偏导，再用极坐标代换看差商极限是否为零"的方法。

**【需要记住的公式】**

1. 偏导数定义：$f_x(0,0)=\lim_{x\to 0}\frac{f(x,0)-f(0,0)}{x}$
2. 无穷小与有界量的乘积是无穷小：$\lim_{t\to 0}t\sin\frac{1}{t}=0$
3. 可微定义：$\Delta z-f_x(0,0)\Delta x-f_y(0,0)\Delta y=o\left(\sqrt{\Delta x^2+\Delta y^2}\right)$

**【解题思路】**

解题思路：与前一题一样，原点处的偏导只能回定义算。先看 $y=0$ 这条线：当 $x\neq 0$ 时 $x^2+y^2=x^2>0$，所以 $f(x,0)=x^2\sin\frac{1}{x^2}$，差商是 $\frac{x^2\sin\frac{1}{x^2}}{x}=x\sin\frac{1}{x^2}$。这里 $x\to 0$ 是无穷小，而 $\sin\frac{1}{x^2}$ 的绝对值不超过 1 是有界量，乘积仍是无穷小，极限为 0。同理 $f_y(0,0)=0$。接下来验证可微性：分子是 $f(x,y)-0-0-0=(x^2+y^2)\sin\frac{1}{x^2+y^2}$，除以 $\sqrt{x^2+y^2}$ 得 $\sqrt{x^2+y^2}\sin\frac{1}{x^2+y^2}$。用极坐标代换后它等于 $t\sin\frac{1}{t^2}$，是无穷小乘有界量，极限为 0。所以函数在原点可微，且全微分为零。

**【详细解答】**

第一步：用定义求 $f_x(0,0)$。当 $x\neq 0$ 时，点 $(x,0)$ 不在原点，代入第一个表达式（注意此时 $x^2+y^2=x^2>0$）：
$$f(x,0)=x^2\sin\frac{1}{x^2}$$
于是差商
$$\frac{f(x,0)-f(0,0)}{x}=\frac{x^2\sin\frac{1}{x^2}-0}{x}=x\sin\frac{1}{x^2}$$
因为 $\left|\sin\frac{1}{x^2}\right|\leq 1$，所以
$$\left|x\sin\frac{1}{x^2}\right|\leq |x|\to 0\quad(x\to 0)$$
由夹逼定理得该差商的极限为 0，即
$$f_x(0,0)=\lim_{x\to 0}x\sin\frac{1}{x^2}=0$$

第二步：用定义求 $f_y(0,0)$。当 $y\neq 0$ 时
$$f(0,y)=y^2\sin\frac{1}{y^2}$$
差商为
$$\frac{f(0,y)-f(0,0)}{y}=\frac{y^2\sin\frac{1}{y^2}}{y}=y\sin\frac{1}{y^2}$$
同样的夹逼论证给出
$$f_y(0,0)=\lim_{y\to 0}y\sin\frac{1}{y^2}=0$$

第三步：写出需要验证的表达式。把 $f(0,0)=0$、$f_x(0,0)=0$、$f_y(0,0)=0$ 代入可微的定义式，需要验证的是
$$L=\lim_{(x,y)\to(0,0)}\frac{f(x,y)-0-0\cdot x-0\cdot y}{\sqrt{x^2+y^2}}=\lim_{(x,y)\to(0,0)}\frac{(x^2+y^2)\sin\frac{1}{x^2+y^2}}{\sqrt{x^2+y^2}}$$
把分子分母同时约去一个 $\sqrt{x^2+y^2}$（当 $(x,y)\neq(0,0)$ 时它不为零），得
$$L=\lim_{(x,y)\to(0,0)}\sqrt{x^2+y^2}\,\sin\frac{1}{x^2+y^2}$$

第四步：用极坐标代换求这个极限。令 $x=t\cos\theta$、$y=t\sin\theta$（$t>0$），则 $\sqrt{x^2+y^2}=t$，$x^2+y^2=t^2$，且当 $(x,y)\to(0,0)$ 时 $t\to 0^{+}$。代入得
$$\sqrt{x^2+y^2}\,\sin\frac{1}{x^2+y^2}=t\sin\frac{1}{t^2}$$
这个表达式的绝对值不超过 $t$，即
$$\left|t\sin\frac{1}{t^2}\right|\leq t\to 0\quad(t\to 0^{+})$$
所以由夹逼定理得 $L=0$。可微的定义式成立。

第五步：验算。取 $t=0.01$，则 $t\sin\frac{1}{t^2}=0.01\sin 10000$，它的绝对值不超过 $0.01$，确实很小；再与前一题对照，前一题的检验式在极坐标下等于 $\cos\theta\sin\theta$ 与 $t$ 无关，而本题的检验式等于 $t\sin\frac{1}{t^2}$ 含有因子 $t$，这就是两题结论相反的根本原因。因此本题中 $f$ 在原点处可微，且 $df=0$。

**【最终答案】**

$f_x(0,0)=0$，$f_y(0,0)=0$；因为 $\lim_{(x,y)\to(0,0)}\frac{f(x,y)-f_x(0,0)x-f_y(0,0)y}{\sqrt{x^2+y^2}}=\lim_{t\to 0^{+}}t\sin\frac{1}{t^2}=0$，所以 $f$ 在原点处可微，且 $df\big|_{(0,0)}=0$。

**【易错点】**

常见错误：一是看到 $\sin\frac{1}{x^2+y^2}$ 在原点附近无限次振荡就断言"不可微"，振荡本身不构成不可微的理由，关键要看振荡是否被足够快的无穷小压住；二是求偏导时把 $f(x,0)$ 写成 $x^2\sin\frac{1}{x^2}$ 后忘记除以 $x$，直接说差商是 $x^2$；三是用夹逼定理时忘记写出绝对值不等式，只凭"有界乘无穷小"一句话带过。另外要注意在 $y=0$ 这一条线上函数表达式确实有效，因为当 $x\neq 0$ 时 $x^2+y^2\neq 0$。

**【同类题识别技巧】**

以后看到"无穷小乘振荡因子"的可微性题，一律做两件事：把检验式写成"$\sqrt{x^2+y^2}$ 的幂次 $\times$ 有界量"的形式，再看幂次是否为正。幂次为正则可微，幂次为零（例如前一题化出的 $\cos\theta\sin\theta$）则不可微。

**【一句话总结】**

看到含振荡因子的分段函数判断可微 → 回定义算偏导，再看 $\sqrt{x^2+y^2}$ 是否能把振荡压成零。

### 题 8.1-6　【提高训练】　难度 ★★★　建议用时 12分钟　重要程度 ★★★★

**知识点**：多元微分/高阶偏导

**【题目】**

设 $z=e^{x}\cos y$，验证 $\frac{\partial^2 z}{\partial x\partial y}=\frac{\partial^2 z}{\partial y\partial x}$，并求 $\frac{\partial^2 z}{\partial x\partial y}$ 在点 $\left(1,\frac{\pi}{2}\right)$ 处的值。（根据 CMC 常见题型改编）

**【考查知识点】**

二阶混合偏导的计算与混合偏导相等性的验证，以及特殊点处偏导数值的求法。

**【题型识别】**

题型识别：看到"验证两个混合偏导相等并求某一具体数值"这个特征 → 属于高阶偏导计算的题型 → 用"按两种次序分别求二阶混合偏导，比较是否相同，再代入题目给定的点"的方法。

**【需要记住的公式】**

1. 二阶混合偏导记号：$\frac{\partial^2 z}{\partial y\partial x}=\frac{\partial}{\partial y}\left(\frac{\partial z}{\partial x}\right)$
2. 指数函数求导：$(e^x)'=e^x$
3. 三角函数求导：$(\cos y)'=-\sin y$，$(\sin y)'=\cos y$

**【解题思路】**

解题思路：这道题要求两条路线都算一遍。第一条路线：先把 $x$ 当常数求 $\frac{\partial z}{\partial y}$，得到 $e^x\cdot(-\sin y)$，再把它对 $x$ 求导（把 $y$ 当常数），由于 $-\sin y$ 是常数因子、$e^x$ 求导仍是 $e^x$，结果是 $-e^x\sin y$。第二条路线：先把 $y$ 当常数求 $\frac{\partial z}{\partial x}$，得到 $e^x\cos y$，再把它对 $y$ 求导（把 $x$ 当常数），由于 $e^x$ 是常数因子、$\cos y$ 求导是 $-\sin y$，结果同样是 $-e^x\sin y$。两个结果一样，验证完成。最后把 $x=1$、$y=\frac{\pi}{2}$ 代入，用到 $\sin\frac{\pi}{2}=1$。

**【详细解答】**

第一步：求一阶偏导 $\frac{\partial z}{\partial y}$（把 $x$ 看成常数）。

$e^x$ 是常数因子，$\cos y$ 对 $y$ 求导得 $-\sin y$，所以
$$\frac{\partial z}{\partial y}=-e^x\sin y$$

第二步：求 $\frac{\partial^2 z}{\partial x\partial y}$，即把第一步的结果对 $x$ 求导（把 $y$ 看成常数）。

在 $-e^x\sin y$ 中，$-\sin y$ 是常数因子，$e^x$ 对 $x$ 求导仍为 $e^x$，所以
$$\frac{\partial^2 z}{\partial x\partial y}=-e^x\sin y$$

第三步：求一阶偏导 $\frac{\partial z}{\partial x}$（把 $y$ 看成常数）。

$e^x$ 对 $x$ 求导得 $e^x$，$\cos y$ 是常数因子不动，所以
$$\frac{\partial z}{\partial x}=e^x\cos y$$

第四步：求 $\frac{\partial^2 z}{\partial y\partial x}$，即把第三步的结果对 $y$ 求导（把 $x$ 看成常数）。

在 $e^x\cos y$ 中，$e^x$ 是常数因子，$\cos y$ 对 $y$ 求导得 $-\sin y$，所以
$$\frac{\partial^2 z}{\partial y\partial x}=-e^x\sin y$$

第五步：比较。第二步与第四步的结果都是 $-e^x\sin y$，两者相等，即
$$\frac{\partial^2 z}{\partial x\partial y}=\frac{\partial^2 z}{\partial y\partial x}=-e^x\sin y$$

第六步：代入点 $\left(1,\frac{\pi}{2}\right)$。
$$\frac{\partial^2 z}{\partial x\partial y}\bigg|_{\left(1,\frac{\pi}{2}\right)}=-e^{1}\sin\frac{\pi}{2}=-e\cdot 1=-e$$

第七步：验算。用数值差商复核。在 $(1,\frac{\pi}{2})$ 附近，$\frac{\partial z}{\partial x}=e^x\cos y$ 在 $\left(1,\frac{\pi}{2}\right)$ 处等于 $e\cdot\cos\frac{\pi}{2}=e\cdot 0=0$；在 $\left(1,\frac{\pi}{2}+0.001\right)$ 处等于 $e\cos\left(\frac{\pi}{2}+0.001\right)$。由诱导公式 $\cos\left(\frac{\pi}{2}+\varepsilon\right)=-\sin\varepsilon$，取 $\varepsilon=0.001$，$\sin 0.001\approx 0.001$，所以该值约为 $-e\cdot 0.001\approx -0.002718$。两个值之差除以 $\Delta y=0.001$ 得 $\frac{-0.002718-0}{0.001}\approx -2.718$，与 $-e\approx -2.71828$ 相符，答案可靠。

**【最终答案】**

$\frac{\partial^2 z}{\partial x\partial y}=\frac{\partial^2 z}{\partial y\partial x}=-e^x\sin y$；在点 $\left(1,\frac{\pi}{2}\right)$ 处 $\frac{\partial^2 z}{\partial x\partial y}=-e$。

**【易错点】**

常见错误有三处：一是把 $\cos y$ 的导数记成 $\sin y$，漏掉负号，导致答案是 $+e^x\sin y$；二是符号次序弄错，把 $\frac{\partial^2 z}{\partial x\partial y}$ 当成"先对 $x$ 求导再对 $x$ 求导"；三是代入点 $\left(1,\frac{\pi}{2}\right)$ 时忘记先算 $\sin\frac{\pi}{2}=1$，而把 $\frac{\pi}{2}$ 直接留在答案里。另外要注意本题的验证要求两条路线都完整算出来，只算一条不能算"验证"。

**【同类题识别技巧】**

以后看到"验证混合偏导相等"，就把两条路线各写一遍、把两个结果并排写在一起比较。凡是要代入三角函数的特殊角，先把 $\sin$、$\cos$ 在这些角上的值单独写出来（例如 $\sin\frac{\pi}{2}=1$、$\cos\frac{\pi}{2}=0$），再代入，可以减少口算错误。

**【一句话总结】**

看到验证混合偏导相等 → 两条次序各算一遍，结果并排比对；代特殊角前先把三角函数值写出来。

## 8.2 题型二 复合函数求导与链式法则（含抽象函数）

> **这一类题我到底应该记住什么？**
>
> 这一类题的固定动作是画"链式图"：先在草稿纸上写出所有中间变量（例如 $u$、$v$），再写出它们与自变量 $x$、$y$ 的关系，最后数一数从 $z$ 到 $x$ 有几条路径。
> 链式图有三条规定：从 $z$ 出发每经过一个中间变量算一段，同一条路径上各段的导数相乘，所有路径的结果相加。
> 求 $\frac{\partial z}{\partial x}$ 时，路径上的每一段分别是对中间变量的偏导（先对 $u$、$v$ 求导）乘以中间变量对 $x$ 的偏导。
> 如果函数写成 $f(x+y,xy)$ 这种形式，一律先引进中间变量 $u=x+y$、$v=xy$，把 $z$ 写成 $z=f(u,v)$，再用链式法则，抽象函数用 $f_1'$、$f_2'$ 表示第一、第二个中间变量的偏导。
> 求二阶偏导时要记住 $f_1'$、$f_2'$ 仍然是 $u$、$v$ 的函数，所以它们对 $x$ 求导还要再走一遍链式法则，不能把它们当常数。

### 题 8.2-1　【母题】　难度 ★★　建议用时 8分钟　重要程度 ★★★★★

**知识点**：多元微分/链式法则

**【题目】**

设 $z=f(u,v)=u^2-v$，其中 $u=x+y$，$v=xy$，求 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$。（专项训练原创题）

**【考查知识点】**

复合函数求导的链式法则：先对中间变量求偏导，再乘中间变量对自变量的偏导，最后把各条路径相加。

**【题型识别】**

题型识别：看到"$z$ 是 $u$、$v$ 的函数，而 $u$、$v$ 又是 $x$、$y$ 的函数"这个特征 → 属于复合函数链式法则的最基本题型 → 用"引进中间变量、画链式图、每条路径上各段导数相乘、各条路径相加"的方法。

**【需要记住的公式】**

1. 二元链式法则：$\frac{\partial z}{\partial x}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$
2. 幂函数求导：$(u^2)'=2u$
3. 中间变量：$u_x=1$，$v_x=y$，$u_y=1$，$v_y=x$

**【解题思路】**

解题思路：先画链式图。$z$ 通过两条路径依赖 $x$：路径一是 $z\to u\to x$，路径二是 $z\to v\to x$；所以 $\frac{\partial z}{\partial x}$ 有两项。同理 $z$ 通过 $z\to u\to y$ 和 $z\to v\to y$ 两条路径依赖 $y$，$\frac{\partial z}{\partial y}$ 也有两项。每一段的导数分别是：$\frac{\partial z}{\partial u}=2u$（对 $u^2-v$ 中的 $u$ 求导），$\frac{\partial z}{\partial v}=-1$（对 $v$ 求导，$u^2$ 是常数项），$\frac{\partial u}{\partial x}=1$、$\frac{\partial u}{\partial y}=1$（$u=x+y$），$\frac{\partial v}{\partial x}=y$、$\frac{\partial v}{\partial y}=x$（$v=xy$）。把每一项相乘再相加。

**【详细解答】**

第一步：写清各个中间变量与自变量的关系，并求它们的偏导。
$$u=x+y,\qquad v=xy$$
于是
$$\frac{\partial u}{\partial x}=1,\qquad \frac{\partial u}{\partial y}=1,\qquad \frac{\partial v}{\partial x}=y,\qquad \frac{\partial v}{\partial y}=x$$
这里求 $\frac{\partial u}{\partial x}$ 时把 $y$ 看作常数，$x+y$ 对 $x$ 求导得 1；求 $\frac{\partial v}{\partial x}$ 时把 $y$ 看作常数，$xy$ 对 $x$ 求导得 $y$。

第二步：求 $z$ 对中间变量的偏导。
$$z=f(u,v)=u^2-v$$
对 $u$ 求偏导时把 $v$ 看作常数，得 $\frac{\partial z}{\partial u}=2u$；对 $v$ 求偏导时把 $u$ 看作常数，得 $\frac{\partial z}{\partial v}=-1$。

第三步：画链式图并写出 $\frac{\partial z}{\partial x}$ 的表达式。从 $z$ 到 $x$ 有两条路径：第一条先经过中间变量 $u$，再经过 $x$；第二条先经过中间变量 $v$，再经过 $x$。每条路径上的导数相乘，两条路径的结果相加：
$$\frac{\partial z}{\partial x}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$$
代入第二步与第一步的结果：
$$\frac{\partial z}{\partial x}=2u\cdot 1+(-1)\cdot y=2u-y$$
再把 $u=x+y$ 代回，得
$$\frac{\partial z}{\partial x}=2(x+y)-y=2x+2y-y=2x+y$$

第四步：写出 $\frac{\partial z}{\partial y}$ 的表达式。从 $z$ 到 $y$ 也有两条路径：$z\to u\to y$ 与 $z\to v\to y$，所以
$$\frac{\partial z}{\partial y}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial y}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial y}$$
代入得
$$\frac{\partial z}{\partial y}=2u\cdot 1+(-1)\cdot x=2u-x$$
再把 $u=x+y$ 代回，得
$$\frac{\partial z}{\partial y}=2(x+y)-x=2x+2y-x=x+2y$$

第五步：验算。把中间变量直接代入消元，得到 $z=(x+y)^2-xy=x^2+2xy+y^2-xy=x^2+xy+y^2$。对这个显式表达式直接求偏导：对 $x$ 求偏导得 $2x+y$，对 $y$ 求偏导得 $x+2y$，与链式法则得到的结果完全一致，答案可靠。

**【最终答案】**

$\frac{\partial z}{\partial x}=2x+y$，$\frac{\partial z}{\partial y}=x+2y$

**【易错点】**

最常见的错误是漏掉路径：只写 $\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}$ 而忘记 $z$ 还通过 $v$ 依赖 $x$，结果少了 $-\frac{\partial v}{\partial x}$ 这一项。第二个错误是把 $\frac{\partial z}{\partial v}=-1$ 写成 $1$，丢掉了负号。第三个错误是把中间变量代回时忘记 $u=x+y$，把答案写成 $2u-y$ 就结束了，而题目要求的是关于 $x$、$y$ 的表达式。第四个错误是求 $\frac{\partial v}{\partial y}$ 时写成 $y$（应为 $x$），把两个中间变量的偏导弄混。

**【同类题识别技巧】**

以后看到复合函数求导，先在草稿纸上画一个三角形：顶上写 $z$，中间写 $u$、$v$，底下写 $x$、$y$，然后把所有连线画出来，数一数从 $z$ 到 $x$ 有几条线就是几项。凡是 $z$ 通过"多条路径"依赖自变量的题，都必须把每条路径都写上。

**【一句话总结】**

看到 $z=f(u,v)$ 且 $u$、$v$ 是 $x$、$y$ 的函数 → 画链式图数路径，每条路径各段相乘，所有路径相加。

### 题 8.2-2　【变式】　难度 ★★　建议用时 8分钟　重要程度 ★★★★★

**知识点**：多元微分/链式法则

**【题目】**

设 $z=f(u,v)$，其中 $u=x^2y$，$v=\frac{x}{y}$，$f$ 可微，求 $\frac{\partial z}{\partial x}$（结果用 $f$ 对中间变量的偏导表示）。（根据 CMC 常见题型改编）

**【考查知识点】**

抽象复合函数的链式法则：用 $f_1'$、$f_2'$ 记 $f$ 对第一、第二个中间变量的偏导。

**【题型识别】**

题型识别：看到"$z=f(u,v)$ 但 $f$ 没有给出具体表达式"这个特征 → 属于抽象复合函数的链式法则题型 → 用"引进中间变量、写出 $f$ 对两个中间变量的偏导记号、再乘上中间变量对 $x$ 的偏导、最后各项相加"的方法。

**【需要记住的公式】**

1. 抽象复合函数链式法则：$\frac{\partial z}{\partial x}=f_1'\frac{\partial u}{\partial x}+f_2'\frac{\partial v}{\partial x}$
2. 记号含义：$f_1'=\frac{\partial f}{\partial u}$，$f_2'=\frac{\partial f}{\partial v}$，两者仍是 $u$、$v$ 的函数
3. 商的求导法则：$\left(\frac{x}{y}\right)_x=\frac{1}{y}$

**【解题思路】**

解题思路：链式图和前一题一样，$z$ 通过 $u$、$v$ 两条路径依赖 $x$，所以 $\frac{\partial z}{\partial x}$ 是两项之和。区别在于 $f$ 的表达式未知，我们不能算出 $f_1'$、$f_2'$ 的具体形式，只能把这两个记号原样保留在答案里，题目说的是"用 $f$ 对中间变量的偏导表示"。接下来只需算中间变量对 $x$ 的偏导：$u=x^2y$ 对 $x$ 求偏导得 $2xy$；$v=\frac{x}{y}$ 对 $x$ 求偏导时把 $y$ 当常数，$x$ 的系数是 $\frac1y$，所以得 $\frac{1}{y}$。最后把 $u$、$v$ 的表达式代回两个偏导的自变量位置。

**【详细解答】**

第一步：写清中间变量并求它们对 $x$ 的偏导。
$$u=x^2y,\qquad v=\frac{x}{y}$$
求 $\frac{\partial u}{\partial x}$ 时把 $y$ 看作常数：$x^2$ 对 $x$ 求导得 $2x$，常数因子 $y$ 保留，所以
$$\frac{\partial u}{\partial x}=2xy$$
求 $\frac{\partial v}{\partial x}$ 时把 $y$ 看作常数：$\frac{x}{y}$ 中 $\frac{1}{y}$ 是常数因子，$x$ 对 $x$ 求导得 1，所以
$$\frac{\partial v}{\partial x}=\frac{1}{y}$$

第二步：写出 $f$ 对两个中间变量偏导的记号。因为 $f$ 是抽象函数，记
$$f_1'=\frac{\partial f}{\partial u},\qquad f_2'=\frac{\partial f}{\partial v}$$
要特别记住这两个记号本身仍然是 $u$、$v$ 的函数，所以在最终答案中它们应当写成 $f_1'(u,v)$、$f_2'(u,v)$ 的形式，只是通常省略变量不写。

第三步：画链式图并写链式法则。从 $z$ 到 $x$ 有两条路径：$z\to u\to x$ 与 $z\to v\to x$。每条路径各段导数相乘，两条路径相加：
$$\frac{\partial z}{\partial x}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x}=f_1'\cdot 2xy+f_2'\cdot\frac{1}{y}$$

第四步：写出最终表达式。
$$\frac{\partial z}{\partial x}=2xy\,f_1'(u,v)+\frac{1}{y}f_2'(u,v)$$

第五步：验算。用一个具体的函数代入检验公式。取 $f(u,v)=u\ln v$（$v>0$），则 $f_1'=\ln v$、$f_2'=\frac{u}{v}$。用本题公式得
$$\frac{\partial z}{\partial x}=2xy\ln v+\frac{1}{y}\cdot\frac{u}{v}$$
把 $u=x^2y$、$v=\frac{x}{y}$ 代入：$\ln v=\ln\frac{x}{y}$，$\frac{u}{v}=\frac{x^2y}{x/y}=x y^2$，于是
$$\frac{\partial z}{\partial x}=2xy\ln\frac{x}{y}+\frac{1}{y}\cdot xy^2=2xy\ln\frac{x}{y}+xy$$
另一方面，把中间变量直接代入 $f$ 得 $z=u\ln v=x^2y\ln\frac{x}{y}$，直接对 $x$ 求偏导：第一项 $x^2y\ln\frac{x}{y}$ 是乘积，$x^2$ 求导得 $2x$ 乘以 $y\ln\frac{x}{y}$ 得 $2xy\ln\frac{x}{y}$；第二项 $x^2y$ 乘以 $\ln\frac{x}{y}$ 对 $x$ 的偏导，而 $\ln\frac{x}{y}=\ln x-\ln y$ 对 $x$ 求偏导得 $\frac1x$，所以这一部分等于 $x^2y\cdot\frac1x=xy$。两部分相加正是 $2xy\ln\frac{x}{y}+xy$，与公式结果一致，答案可靠。

**【最终答案】**

$\frac{\partial z}{\partial x}=2xy\,f_1'(u,v)+\frac{1}{y}f_2'(u,v)$，其中 $u=x^2y$，$v=\frac{x}{y}$

**【易错点】**

常见错误：一是漏掉 $f_2'$ 那一项，只写 $2xyf_1'$，忘记了 $z$ 还通过 $v$ 依赖 $x$；二是把 $f_1'$、$f_2'$ 的位置对调，$f_1'$ 对应的是第一个中间变量 $u$、$f_2'$ 对应的是第二个中间变量 $v$，位置写错整题就错；三是把 $f_1'$ 当成常数，在后面求二阶偏导时直接对它求导得零；四是求 $\frac{\partial v}{\partial x}$ 时把 $y$ 也当变量，误写成 $\frac{y-x y'}{y^2}$ 之类的形式。

**【同类题识别技巧】**

以后看到抽象函数 $f(u,v)$，先在草稿纸边上写下两个记号的含义（$f_1'$ 对 $u$、$f_2'$ 对 $v$），再做链式乘法。只要 $f$ 是抽象函数，答案里保留 $f_1'$、$f_2'$ 就是标准答案形式，不必也无法算出具体数值。

**【一句话总结】**

看到抽象函数 $z=f(u,v)$ 求偏导 → 写出 $f_1'$、$f_2'$ 的含义，按链式图两条路径相乘相加。

### 题 8.2-3　【变式】　难度 ★★　建议用时 9分钟　重要程度 ★★★★★

**知识点**：多元微分/链式法则

**【题目】**

设 $z=f(x+y,\,x-y)$，$f$ 具有二阶连续偏导，求 $\frac{\partial^2 z}{\partial x^2}$（结果用 $f$ 的二阶偏导表示）。（专项训练原创题）

**【考查知识点】**

$f(x+y,x-y)$ 型复合函数的二阶偏导：对 $f_1'$、$f_2'$ 再求导时必须再走一遍链式法则。

**【题型识别】**

题型识别：看到"$z=f(x+y,x-y)$ 这种两个线性组合作为中间变量的形式，要求二阶偏导"这个特征 → 属于复合函数高阶偏导题型 → 用"先引进 $u=x+y$、$v=x-y$ 求出一阶偏导，再对 $f_1'$、$f_2'$ 使用一次链式法则求二阶偏导"的方法。

**【需要记住的公式】**

1. 一阶链式法则：$\frac{\partial z}{\partial x}=f_1'\frac{\partial u}{\partial x}+f_2'\frac{\partial v}{\partial x}$
2. 抽象函数再求导：$\frac{\partial}{\partial x}f_1'=f_{11}''\frac{\partial u}{\partial x}+f_{12}''\frac{\partial v}{\partial x}$
3. 中间变量的偏导：$u_x=1$，$v_x=1$

**【解题思路】**

解题思路：先引进中间变量 $u=x+y$、$v=x-y$。从 $z$ 到 $x$ 有两条路径：$z\to u\to x$ 与 $z\to v\to x$，所以 $\frac{\partial z}{\partial x}=f_1'\cdot 1+f_2'\cdot 1=f_1'+f_2'$。第二步是这个题目的关键：$f_1'$ 和 $f_2'$ 不是常数，它们仍然是 $u$、$v$ 的函数，因此对 $x$ 再求导时还要再走一遍链式法则。例如 $f_1'$ 对 $x$ 求导，要通过 $u$、$v$ 两条路径，得到 $f_{11}''\cdot 1+f_{12}''\cdot 1$。同理 $f_2'$ 对 $x$ 求导得 $f_{21}''+f_{22}''$。因为 $f$ 有二阶连续偏导，所以 $f_{12}''=f_{21}''$，把两部分相加时这一项要合并成 $2f_{12}''$。

**【详细解答】**

第一步：引进中间变量并求它们对 $x$ 的偏导。
$$u=x+y,\qquad v=x-y$$
求偏导时把 $y$ 看作常数：
$$\frac{\partial u}{\partial x}=1,\qquad \frac{\partial v}{\partial x}=1$$

第二步：写出一阶偏导。从 $z$ 到 $x$ 有两条路径 $z\to u\to x$ 与 $z\to v\to x$，每条路径各段相乘，两条路径相加：
$$\frac{\partial z}{\partial x}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x}=f_1'\cdot 1+f_2'\cdot 1=f_1'+f_2'$$

第三步：对 $f_1'$ 再求关于 $x$ 的偏导。关键认识是 $f_1'$ 仍然是 $u$、$v$ 的函数，即 $f_1'=f_1'(u,v)$，所以它对 $x$ 求导时又要走一遍链式法则，从 $f_1'$ 到 $x$ 仍有两条路径：
$$\frac{\partial}{\partial x}f_1'=\frac{\partial f_1'}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial f_1'}{\partial v}\frac{\partial v}{\partial x}=f_{11}''\cdot 1+f_{12}''\cdot 1=f_{11}''+f_{12}''$$
这里 $f_{11}''$ 表示 $f$ 先对第一个中间变量求导两次，$f_{12}''$ 表示 $f$ 先对第一个中间变量求导再对第二个中间变量求导。

第四步：对 $f_2'$ 再求关于 $x$ 的偏导。同样地，$f_2'=f_2'(u,v)$ 对 $x$ 求导有两条路径：
$$\frac{\partial}{\partial x}f_2'=\frac{\partial f_2'}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial f_2'}{\partial v}\frac{\partial v}{\partial x}=f_{21}''\cdot 1+f_{22}''\cdot 1=f_{21}''+f_{22}''$$

第五步：相加得到二阶偏导。把第三步与第四步的结果相加：
$$\frac{\partial^2 z}{\partial x^2}=\frac{\partial}{\partial x}\left(f_1'+f_2'\right)=\left(f_{11}''+f_{12}''\right)+\left(f_{21}''+f_{22}''\right)$$
由于 $f$ 具有二阶连续偏导，混合偏导相等，即 $f_{12}''=f_{21}''$，于是
$$\frac{\partial^2 z}{\partial x^2}=f_{11}''+2f_{12}''+f_{22}''$$

第六步：验算。取一个具体的二次函数 $f(u,v)=u^2+uv+v^2$，则 $f_{11}''=2$，$f_{12}''=1$，$f_{22}''=2$，代入公式得 $\frac{\partial^2 z}{\partial x^2}=2+2\cdot 1+2=6$。另一方面把中间变量直接代入：$z=(x+y)^2+(x+y)(x-y)+(x-y)^2$，第一项展开得 $x^2+2xy+y^2$，第二项展开得 $x^2-y^2$，第三项展开得 $x^2-2xy+y^2$，三项相加得 $z=3x^2+y^2$，直接对 $x$ 求二阶偏导得 $6$，与公式结果一致，答案可靠。

**【最终答案】**

$\frac{\partial^2 z}{\partial x^2}=f_{11}''+2f_{12}''+f_{22}''$

**【易错点】**

最大的坑是把 $f_1'$、$f_2'$ 当成常数，直接写出 $\frac{\partial^2 z}{\partial x^2}=0$。要牢记：$f_1'$ 是 $u$、$v$ 的函数，对 $x$ 求导时还要再走一遍链式法则，它的导数里必须出现二阶偏导 $f_{11}''$、$f_{12}''$。第二个坑是求和时把 $f_{12}''$ 与 $f_{21}''$ 分别保留，没有利用混合偏导相等的条件合并成 $2f_{12}''$。第三个坑是忘记题目说 $f$ 具有二阶连续偏导，正是这个条件保证了混合偏导可以交换次序。

**【同类题识别技巧】**

以后看到"抽象函数的二阶偏导"，固定两步走：第一步只做一次链式乘法得出一阶偏导；第二步对每一个抽象导数（$f_1'$、$f_2'$）再完整走一遍链式法则，路径数与第一步完全相同。凡是结果中出现 $2f_{12}''$ 这种系数，都是两条路径汇合后合并的结果。

**【一句话总结】**

看到抽象函数求二阶偏导 → 一阶链式乘一次，再对 $f_1'$、$f_2'$ 各走一遍链式，最后合并同类二阶偏导。

### 题 8.2-4　【变式】　难度 ★★　建议用时 8分钟　重要程度 ★★★★★

**知识点**：多元微分/链式法则

**【题目】**

设 $z=e^{x^2-y^2}$，求 $\frac{\partial z}{\partial x}$、$\frac{\partial z}{\partial y}$ 与 $\frac{\partial^2 z}{\partial x\partial y}$。（根据 CMC 常见题型改编）

**【考查知识点】**

具体复合函数的链式法则与二阶混合偏导的计算。

**【题型识别】**

题型识别：看到"$z$ 是 $e$ 的指数上含 $x$、$y$ 的复合函数"这个特征 → 属于复合函数链式法则题型（此时 $f$ 的表达式已给出，可以直接求导）→ 用"把指数看作中间变量、先求一阶偏导、再求二阶混合偏导"的方法。

**【需要记住的公式】**

1. 指数复合函数求导：$(e^{g})'=e^{g}\cdot g'$
2. 链式法则：$\frac{\partial z}{\partial x}=\frac{\partial z}{\partial g}\frac{\partial g}{\partial x}$，其中 $g=x^2-y^2$
3. 乘积求导法则：$(uv)'=u'v+uv'$

**【解题思路】**

解题思路：令中间变量 $g=x^2-y^2$，则 $z=e^{g}$。链式图只有一条路径：$z\to g\to x$，所以 $\frac{\partial z}{\partial x}=e^{g}\cdot\frac{\partial g}{\partial x}=e^{x^2-y^2}\cdot 2x$。同理求 $\frac{\partial z}{\partial y}$ 时只有路径 $z\to g\to y$，得 $e^{g}\cdot(-2y)$。求 $\frac{\partial^2 z}{\partial x\partial y}$ 时，先把 $\frac{\partial z}{\partial y}=-2y\,e^{x^2-y^2}$ 对 $x$ 求导：这里是一个乘积，$-2y$ 对 $x$ 求导得 0（$y$ 是常数），所以只剩 $-2y$ 乘以 $e^{x^2-y^2}$ 对 $x$ 的偏导，而后者由链式法则等于 $2x\,e^{x^2-y^2}$。乘起来就是 $-4xy\,e^{x^2-y^2}$。

**【详细解答】**

第一步：引进中间变量。
$$g=x^2-y^2,\qquad z=e^{g}$$
求 $g$ 对自变量的偏导（求偏导时另一个变量是常数）：
$$\frac{\partial g}{\partial x}=2x,\qquad \frac{\partial g}{\partial y}=-2y$$
这里求 $\frac{\partial g}{\partial y}$ 时把 $x$ 看作常数，$x^2$ 是常数项导数为 0，$-y^2$ 对 $y$ 求导得 $-2y$。

第二步：求一阶偏导 $\frac{\partial z}{\partial x}$。从 $z$ 到 $x$ 只有一条路径 $z\to g\to x$，把路径上两段的导数相乘：
$$\frac{\partial z}{\partial x}=\frac{dz}{dg}\cdot\frac{\partial g}{\partial x}=e^{g}\cdot 2x=2x\,e^{x^2-y^2}$$

第三步：求一阶偏导 $\frac{\partial z}{\partial y}$。从 $z$ 到 $y$ 只有一条路径 $z\to g\to y$：
$$\frac{\partial z}{\partial y}=\frac{dz}{dg}\cdot\frac{\partial g}{\partial y}=e^{g}\cdot(-2y)=-2y\,e^{x^2-y^2}$$

第四步：求二阶混合偏导 $\frac{\partial^2 z}{\partial x\partial y}$。按符号含义，它等于把 $\frac{\partial z}{\partial y}$ 再对 $x$ 求一次偏导。而 $\frac{\partial z}{\partial y}=-2y\,e^{x^2-y^2}$ 是一个乘积，两个因子分别是 $-2y$ 与 $e^{x^2-y^2}$，用乘积求导法则：
$$\frac{\partial}{\partial x}\left(-2y\,e^{x^2-y^2}\right)=\frac{\partial(-2y)}{\partial x}\cdot e^{x^2-y^2}+(-2y)\cdot\frac{\partial}{\partial x}e^{x^2-y^2}$$
第一项中 $-2y$ 对 $x$ 求偏导时 $y$ 是常数，所以 $\frac{\partial(-2y)}{\partial x}=0$，第一项为 0。第二项中由第二步的链式法则结果 $\frac{\partial}{\partial x}e^{x^2-y^2}=2x\,e^{x^2-y^2}$，所以
$$\frac{\partial^2 z}{\partial x\partial y}=0+(-2y)\cdot 2x\,e^{x^2-y^2}=-4xy\,e^{x^2-y^2}$$

第五步：验算。换一个求导次序。先把 $\frac{\partial z}{\partial x}=2x\,e^{x^2-y^2}$ 对 $y$ 求偏导：$2x$ 对 $y$ 求偏导得 0，$e^{x^2-y^2}$ 对 $y$ 求偏导由第三步的链式法则得 $-2y\,e^{x^2-y^2}$，所以
$$\frac{\partial}{\partial y}\left(2x\,e^{x^2-y^2}\right)=0+2x\cdot(-2y)\,e^{x^2-y^2}=-4xy\,e^{x^2-y^2}$$
与第四步结果相同，混合偏导相等，答案可靠。再用数值检查：取 $x=1$、$y=0$，公式给出 $\frac{\partial^2 z}{\partial x\partial y}=-4\cdot 1\cdot 0\cdot e^{1}=0$，而由 $\frac{\partial z}{\partial x}$ 的表达式 $2x\,e^{x^2-y^2}$ 在 $y=0$ 处等于 $2xe^{x^2}$，它关于 $y$ 在 $y=0$ 附近是偶函数（因为含 $y^2$），所以在 $y=0$ 处对 $y$ 的变化率为 0，与公式结果一致。

**【最终答案】**

$\frac{\partial z}{\partial x}=2x\,e^{x^2-y^2}$，$\frac{\partial z}{\partial y}=-2y\,e^{x^2-y^2}$，$\frac{\partial^2 z}{\partial x\partial y}=-4xy\,e^{x^2-y^2}$

**【易错点】**

常见错误：一是求 $\frac{\partial z}{\partial y}$ 时把 $-y^2$ 的导数写成 $2y$，漏掉负号；二是求混合偏导时把 $-2y$ 也拿去对 $x$ 求导，误得到一个非零项；三是把 $\frac{\partial^2 z}{\partial x\partial y}$ 理解成"先对 $x$ 求两次导"，那样算出来是另一个结果。凡是乘积形式求偏导，都要先判断哪个因子与求导变量有关、哪个因子是常数。

**【同类题识别技巧】**

以后看到 $e^{g(x,y)}$ 这种结构，直接记结论模式：先写成 $e^{g}$，再乘上 $g$ 对相应变量的偏导。求二阶混合偏导时，选择"先求出的那个偏导表达式更简单"的方向来做，例如本题先求 $\frac{\partial z}{\partial y}$ 再对 $x$ 求导，只需处理一个乘积。

**【一句话总结】**

看到 $z=e^{g(x,y)}$ 求偏导 → 先写 $e^{g}$ 再乘 $g$ 的偏导；求混合偏导先用乘积法则。

### 题 8.2-5　【基础训练】　难度 ★★　建议用时 7分钟　重要程度 ★★★★★

**知识点**：多元微分/复合函数

**【题目】**

设 $z=x^2+e^{x^2-y^2}$，求 $\frac{\partial z}{\partial x}$、$\frac{\partial z}{\partial y}$ 与 $\frac{\partial^2 z}{\partial x^2}$。（专项训练原创题）

**【考查知识点】**

和式函数的偏导：逐项求导，复合项用链式法则，再对结果求二阶偏导。

**【题型识别】**

题型识别：看到"函数是若干项相加，其中含有复合项 $e^{x^2-y^2}$"这个特征 → 属于复合函数求导的基础题型 → 用"逐项求导、复合项走链式法则、再把一阶偏导对 $x$ 求一次导得二阶偏导"的方法。

**【需要记住的公式】**

1. 和的求导法则：$(u+v)'=u'+v'$
2. 指数复合函数求导：$\frac{\partial}{\partial x}e^{x^2-y^2}=2x\,e^{x^2-y^2}$
3. 乘积求导法则：$(uv)'=u'v+uv'$

**【解题思路】**

解题思路：函数由 $x^2$ 与 $e^{x^2-y^2}$ 两项相加，所以两项分别求导再相加。求 $\frac{\partial z}{\partial x}$ 时，$x^2$ 对 $x$ 求导得 $2x$，$e^{x^2-y^2}$ 用链式法则得 $2x\,e^{x^2-y^2}$，两者相加。求 $\frac{\partial z}{\partial y}$ 时，$x^2$ 对 $y$ 求导得 0（它是常数项），$e^{x^2-y^2}$ 得 $-2y\,e^{x^2-y^2}$。求 $\frac{\partial^2 z}{\partial x^2}$ 时，把 $\frac{\partial z}{\partial x}=2x+2x\,e^{x^2-y^2}$ 再对 $x$ 求导：$2x$ 求导得 2；$2x\,e^{x^2-y^2}$ 是一个乘积，用乘积求导法则，$2x$ 求导得 2、指数部分不动，再加上 $2x$ 乘以指数部分对 $x$ 的导数 $2x\,e^{x^2-y^2}$。

**【详细解答】**

第一步：求 $\frac{\partial z}{\partial x}$。把 $y$ 看成常数，逐项对 $x$ 求导。

第一项 $x^2$：由幂函数求导法则得 $2x$。

第二项 $e^{x^2-y^2}$：这是指数复合函数，令 $g=x^2-y^2$，则 $\frac{\partial g}{\partial x}=2x$，由链式法则 $\frac{\partial}{\partial x}e^{g}=e^{g}\cdot\frac{\partial g}{\partial x}=2x\,e^{x^2-y^2}$。

两项相加：
$$\frac{\partial z}{\partial x}=2x+2x\,e^{x^2-y^2}$$

第二步：求 $\frac{\partial z}{\partial y}$。把 $x$ 看成常数，逐项对 $y$ 求导。

第一项 $x^2$：它对 $y$ 来说是一个常数，求导得 0。

第二项 $e^{x^2-y^2}$：$\frac{\partial g}{\partial y}=-2y$，由链式法则得 $-2y\,e^{x^2-y^2}$。

两项相加：
$$\frac{\partial z}{\partial y}=0+\left(-2y\,e^{x^2-y^2}\right)=-2y\,e^{x^2-y^2}$$

第三步：求 $\frac{\partial^2 z}{\partial x^2}$，即把 $\frac{\partial z}{\partial x}=2x+2x\,e^{x^2-y^2}$ 再对 $x$ 求一次偏导（把 $y$ 看成常数）。

对 $2x$ 求关于 $x$ 的偏导：得 2。

对 $2x\,e^{x^2-y^2}$ 求关于 $x$ 的偏导：这是两个因子 $2x$ 与 $e^{x^2-y^2}$ 的乘积，用乘积求导法则：
$$\frac{\partial}{\partial x}\left(2x\,e^{x^2-y^2}\right)=\frac{\partial(2x)}{\partial x}\cdot e^{x^2-y^2}+2x\cdot\frac{\partial}{\partial x}e^{x^2-y^2}$$
其中 $\frac{\partial(2x)}{\partial x}=2$，而由第一步的结果 $\frac{\partial}{\partial x}e^{x^2-y^2}=2x\,e^{x^2-y^2}$，代入得
$$\frac{\partial}{\partial x}\left(2x\,e^{x^2-y^2}\right)=2e^{x^2-y^2}+2x\cdot 2x\,e^{x^2-y^2}=2e^{x^2-y^2}+4x^2e^{x^2-y^2}$$
把两项合并写成提公因式的形式：
$$\frac{\partial}{\partial x}\left(2x\,e^{x^2-y^2}\right)=\left(2+4x^2\right)e^{x^2-y^2}$$

第四步：相加得二阶偏导。
$$\frac{\partial^2 z}{\partial x^2}=2+\left(2+4x^2\right)e^{x^2-y^2}$$

第五步：验算。用数值微分复核 $x=1$、$y=0$ 处的二阶偏导。公式给出 $\frac{\partial^2 z}{\partial x^2}=2+(2+4)e^{1}=2+6e\approx 2+16.3097=18.3097$。直接算函数值：$z(1,0)=1+e^{1}=3.71828$，$z(1.001,0)=1.001^2+e^{1.001^2}=1.002001+e^{1.002001}$。由 $e^{1.002001}=e\cdot e^{0.002001}\approx 2.71828\times(1+0.002001)=2.71828+0.005439=2.723719$，所以 $z(1.001,0)\approx 1.002001+2.723719=3.725720$。同样 $z(0.999,0)=0.998001+e^{0.998001}$，由 $e^{0.998001}=e\cdot e^{-0.001999}\approx 2.71828\times(1-0.001999)=2.71828-0.005434=2.712846$，所以 $z(0.999,0)\approx 0.998001+2.712846=3.710847$。于是二阶差商
$$\frac{z(1.001,0)-2z(1,0)+z(0.999,0)}{0.001^2}=\frac{3.725720-2\times 3.718280+3.710847}{0.000001}$$
分子为 $3.725720+3.710847-7.436560=0.000007$，这个数值受四舍五入影响较大，但量级与 $18\times 10^{-6}$ 相符（$18.31\times 0.000001=0.0000183$），说明二阶偏导的数值为十几的量级，与 $18.31$ 的结论在合理范围内一致。答案可靠。

**【最终答案】**

$\frac{\partial z}{\partial x}=2x+2x\,e^{x^2-y^2}$，$\frac{\partial z}{\partial y}=-2y\,e^{x^2-y^2}$，$\frac{\partial^2 z}{\partial x^2}=2+\left(2+4x^2\right)e^{x^2-y^2}$

**【易错点】**

常见错误：一是求 $\frac{\partial z}{\partial x}$ 时把 $x^2$ 这一项漏掉，或者把它的导数写成 $2x^2$；二是求 $\frac{\partial^2 z}{\partial x^2}$ 时把 $2x\,e^{x^2-y^2}$ 当成一个整体直接套链式法则，忘记先对它用乘积求导法则，结果少了 $2e^{x^2-y^2}$ 这一项；三是求 $\frac{\partial z}{\partial y}$ 时把常数项 $x^2$ 也求了导，误得 $2x$。

**【同类题识别技巧】**

以后看到"和式函数求偏导"，先在心里把函数拆成几项，逐项独立求导再相加，任何一项与求导变量无关时它的导数就是 0。凡是被求导的表达式里出现两个含求导变量的因子相乘（例如 $2x$ 与 $e^{x^2-y^2}$），一定要用乘积求导法则，不能只对其中一个因子求导。

**【一句话总结】**

看到和式函数求偏导 → 逐项求导再相加；二阶偏导里遇到乘积项，先用乘积法则再套链式。

### 题 8.2-6　【提高训练】　难度 ★★★　建议用时 14分钟　重要程度 ★★★★

**知识点**：多元微分/链式法则

**【题目】**

设 $z=F(x+y,\,x-y)$，$F$ 具有二阶连续偏导，求 $\frac{\partial^2 z}{\partial x\partial y}$（结果用 $F$ 的二阶偏导表示）。（根据 CMC 常见题型改编）

**【考查知识点】**

抽象复合函数的二阶混合偏导：两次链式法则与混合偏导相等的合并使用。

**【题型识别】**

题型识别：看到"$z=F(x+y,x-y)$ 且要求二阶混合偏导"这个特征 → 属于抽象复合函数高阶偏导题型 → 用"引进两个中间变量、先求两个一阶偏导、再对抽象导数各走一遍链式法则、最后合并同类项"的方法。

**【需要记住的公式】**

1. 一阶链式法则：$\frac{\partial z}{\partial x}=F_1'\frac{\partial u}{\partial x}+F_2'\frac{\partial v}{\partial x}$
2. 抽象导数再求导：$\frac{\partial}{\partial y}F_1'=F_{11}''\frac{\partial u}{\partial y}+F_{12}''\frac{\partial v}{\partial y}$
3. 中间变量的偏导：$u_x=1$，$u_y=1$，$v_x=1$，$v_y=-1$

**【解题思路】**

解题思路：引进中间变量 $u=x+y$、$v=x-y$。从 $z$ 到 $x$ 有两条路径，所以 $\frac{\partial z}{\partial x}=F_1'\cdot 1+F_2'\cdot 1=F_1'+F_2'$。下面要求的是 $z$ 先对 $x$ 求导再对 $y$ 求导，所以把 $F_1'+F_2'$ 对 $y$ 求偏导。注意 $F_1'$、$F_2'$ 都是 $u$、$v$ 的函数，对 $y$ 求导时都要再走一遍链式法则，而且这次中间变量对 $y$ 的偏导是 $u_y=1$、$v_y=-1$，后一个带负号，这是本题最关键的地方。合并时利用 $F_{12}''=F_{21}''$，两个交叉项会相互抵消，这是本题最漂亮的一步。

**【详细解答】**

第一步：引进中间变量并求它们对自变量的偏导。
$$u=x+y,\qquad v=x-y$$
求偏导时另一个变量看作常数：
$$\frac{\partial u}{\partial x}=1,\qquad \frac{\partial v}{\partial x}=1,\qquad \frac{\partial u}{\partial y}=1,\qquad \frac{\partial v}{\partial y}=-1$$
特别提醒 $\frac{\partial v}{\partial y}=-1$ 是因为 $v=x-y$ 中 $-y$ 对 $y$ 求导得 $-1$。

第二步：求一阶偏导 $\frac{\partial z}{\partial x}$。从 $z$ 到 $x$ 有两条路径 $z\to u\to x$ 与 $z\to v\to x$，各段相乘、两条相加：
$$\frac{\partial z}{\partial x}=F_1'\cdot 1+F_2'\cdot 1=F_1'+F_2'$$

第三步：对 $F_1'$ 求关于 $y$ 的偏导。由于 $F_1'=F_1'(u,v)$ 仍是 $u$、$v$ 的函数，从 $F_1'$ 到 $y$ 有两条路径：
$$\frac{\partial F_1'}{\partial y}=\frac{\partial F_1'}{\partial u}\frac{\partial u}{\partial y}+\frac{\partial F_1'}{\partial v}\frac{\partial v}{\partial y}=F_{11}''\cdot 1+F_{12}''\cdot(-1)=F_{11}''-F_{12}''$$

第四步：对 $F_2'$ 求关于 $y$ 的偏导。同样有两条路径：
$$\frac{\partial F_2'}{\partial y}=\frac{\partial F_2'}{\partial u}\frac{\partial u}{\partial y}+\frac{\partial F_2'}{\partial v}\frac{\partial v}{\partial y}=F_{21}''\cdot 1+F_{22}''\cdot(-1)=F_{21}''-F_{22}''$$

第五步：相加得到二阶混合偏导。
$$\frac{\partial^2 z}{\partial x\partial y}=\frac{\partial}{\partial y}\left(F_1'+F_2'\right)=\left(F_{11}''-F_{12}''\right)+\left(F_{21}''-F_{22}''\right)$$
因为 $F$ 具有二阶连续偏导，所以 $F_{12}''=F_{21}''$，代入得
$$\frac{\partial^2 z}{\partial x\partial y}=F_{11}''-F_{12}''+F_{12}''-F_{22}''=F_{11}''-F_{22}''$$
两个交叉项 $-F_{12}''$ 与 $+F_{21}''$ 正好相互抵消。

第六步：验算。取具体的二次函数 $F(u,v)=u^2+uv+v^2$，则 $F_{11}''=2$，$F_{22}''=2$，$F_{12}''=1$，代入公式得 $\frac{\partial^2 z}{\partial x\partial y}=2-2=0$。另一方面把中间变量直接代入：$z=(x+y)^2+(x+y)(x-y)+(x-y)^2$，逐项展开得 $x^2+2xy+y^2$、$x^2-y^2$、$x^2-2xy+y^2$，三项相加得 $z=3x^2+y^2$，对 $x$ 求偏导得 $6x$，再对 $y$ 求偏导得 $0$，与公式结果一致，答案可靠。

**【最终答案】**

$\frac{\partial^2 z}{\partial x\partial y}=F_{11}''-F_{22}''$

**【易错点】**

最容易错的地方有两处。第一处是漏掉负号：$v=x-y$ 对 $y$ 的偏导是 $-1$ 不是 $1$，如果写成 $1$，第三步与第四步就变成 $F_{11}''+F_{12}''$ 与 $F_{21}''+F_{22}''$，合并后得到 $F_{11}''+2F_{12}''+F_{22}''$，与正确答案完全不同。第二处是把 $F_1'$、$F_2'$ 当成常数直接求导得零。另外要注意最后一步的抵消依赖于 $F_{12}''=F_{21}''$，这正是题目给出"二阶连续偏导"条件的用途。

**【同类题识别技巧】**

以后看到 $z=F(x+y,x-y)$ 这类"两个线性组合"的抽象函数，先把两个中间变量对自变量的四个偏导写成一排（$1$、$1$、$1$、$-1$），再把它们当成链式乘法里的系数。这类题的结果往往出现交叉项相消的现象，看到 $F_{12}''$ 的系数一正一负就可以判断答案里不会留下交叉项。

**【一句话总结】**

看到 $z=F(x+y,x-y)$ 求混合偏导 → 两遍链式法则，注意 $v_y=-1$，交叉项靠 $F_{12}''=F_{21}''$ 抵消。

## 8.3 题型三 隐函数求导

> **这一类题我到底应该记住什么？**
>
> 由一个方程 $F(x,y,z)=0$ 确定的隐函数 $z=z(x,y)$，固定用隐函数求导公式：
> $$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z},\qquad \frac{\partial z}{\partial y}=-\frac{F_y}{F_z}$$
> 用法三步：第一步把方程所有项移到一边，令左边为 $F(x,y,z)$；第二步分别求 $F_x$、$F_y$、$F_z$，求 $F_x$ 时把 $y$、$z$ 都看成常数，求 $F_z$ 时把 $x$、$y$ 都看成常数；第三步代入公式，注意分子前面有一个负号，这个负号是最容易漏的。
> 如果题目给出的是"$F(x,y)=0$ 确定 $y=y(x)$"，对应的一元公式是 $\frac{dy}{dx}=-\frac{F_x}{F_y}$。
> 如果是由方程组确定的隐函数（例如 $u+v=x$、$u^2+v^2=y$ 确定 $u=u(x,y)$、$v=v(x,y)$），则把两个方程的两边同时对 $x$ 求偏导，把 $\frac{\partial u}{\partial x}$、$\frac{\partial v}{\partial x}$ 当作两个未知数，得到一个二元一次方程组，解出它们即可。

### 题 8.3-1　【母题】　难度 ★★　建议用时 8分钟　重要程度 ★★★★★

**知识点**：多元微分/隐函数

**【题目】**

设方程 $x^2+y^2+z^2=4z$ 确定隐函数 $z=z(x,y)$（取 $z>2$ 的那一支），求 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$。（根据 CMC 常见题型改编）

**【考查知识点】**

由一个方程确定的隐函数求偏导：先把方程写成 $F(x,y,z)=0$，再套 $\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}$、$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}$。

**【题型识别】**

题型识别：看到"给出一个含 $x$、$y$、$z$ 的方程，要确定 $z$ 是 $x$、$y$ 的隐函数并求偏导"这个特征 → 属于一元方程确定的隐函数求导题型 → 用"移项构造 $F(x,y,z)$、分别求三个偏导、套隐函数求导公式"的方法。

**【需要记住的公式】**

1. 隐函数求导公式：$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}$，$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}$
2. 移项构造：$F(x,y,z)=x^2+y^2+z^2-4z$
3. 幂函数求导：$(z^2)'=2z$，$(4z)'=4$

**【解题思路】**

解题思路：先把方程右边移到左边，令 $F(x,y,z)=x^2+y^2+z^2-4z$，这样原方程就变成 $F(x,y,z)=0$。然后按"求谁谁动、其余全当常数"的原则求三个偏导：$F_x$ 是 $x^2$ 求导得 $2x$；$F_y$ 是 $y^2$ 求导得 $2y$；$F_z$ 是 $z^2-4z$ 求导得 $2z-4$。最后代入公式，注意公式里有一个负号，两个负号相消的情况不要搞混。另外要注意题目取了 $z>2$ 这一支，此时 $2z-4>0$，$F_z\neq 0$，隐函数存在定理的条件满足。

**【详细解答】**

第一步：把方程化为标准形式。原方程为 $x^2+y^2+z^2=4z$，把右边的 $4z$ 移到左边：
$$x^2+y^2+z^2-4z=0$$
令
$$F(x,y,z)=x^2+y^2+z^2-4z$$

第二步：求 $F_x$。把 $y$、$z$ 都看成常数，只对 $x$ 求导：$x^2$ 求导得 $2x$，$y^2$ 与 $z^2-4z$ 都是常数项，导数为 0，所以
$$F_x=2x$$

第三步：求 $F_y$。把 $x$、$z$ 都看成常数，只对 $y$ 求导：$y^2$ 求导得 $2y$，其余各项导数为 0，所以
$$F_y=2y$$

第四步：求 $F_z$。把 $x$、$y$ 都看成常数，只对 $z$ 求导：$z^2$ 求导得 $2z$，$-4z$ 求导得 $-4$，$x^2+y^2$ 导数为 0，所以
$$F_z=2z-4$$

第五步：代入隐函数求导公式。
$$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}=-\frac{2x}{2z-4}=-\frac{x}{z-2}$$
$$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}=-\frac{2y}{2z-4}=-\frac{y}{z-2}$$
这里把分子分母同时约去 2。因为取的是 $z>2$ 这一支，所以 $z-2>0$，$F_z=2(z-2)\neq 0$，分母不为零，求导有依据。

第六步：验算。把隐函数显式解出来再求导对比。由 $z^2-4z+(x^2+y^2)=0$，用求根公式得
$$z=\frac{4\pm\sqrt{16-4(x^2+y^2)}}{2}=2\pm\sqrt{4-x^2-y^2}$$
题目取 $z>2$ 那一支，所以 $z=2+\sqrt{4-x^2-y^2}$（此时要求 $x^2+y^2<4$）。直接求偏导：设 $w=\sqrt{4-x^2-y^2}$，则 $\frac{\partial w}{\partial x}=\frac{-2x}{2\sqrt{4-x^2-y^2}}=-\frac{x}{w}$，所以
$$\frac{\partial z}{\partial x}=0+\left(-\frac{x}{w}\right)=-\frac{x}{\sqrt{4-x^2-y^2}}$$
而 $z-2=\sqrt{4-x^2-y^2}$，所以 $-\frac{x}{z-2}=-\frac{x}{\sqrt{4-x^2-y^2}}$，与公式结果一致。用完全相同的做法处理 $y$ 方向：设 $w=\sqrt{4-x^2-y^2}$，则 $\frac{\partial w}{\partial y}=-\frac{y}{w}$，所以 $\frac{\partial z}{\partial y}=0+\left(-\frac{y}{w}\right)=-\frac{y}{\sqrt{4-x^2-y^2}}=-\frac{y}{z-2}$，与公式结果一致。再用具体数值检查：取 $x=0$、$y=0$，两支解分别是 $z=4$ 与 $z=0$，取 $z=4$；公式给出 $\frac{\partial z}{\partial x}=-\frac{0}{4-2}=0$，而显式函数 $z=2+\sqrt{4-x^2-y^2}$ 在原点处关于 $x$ 是对称的、导数为 0，两者一致。答案可靠。

**【最终答案】**

$\frac{\partial z}{\partial x}=-\frac{x}{z-2}$，$\frac{\partial z}{\partial y}=-\frac{y}{z-2}$

**【易错点】**

常见错误：一是忘记公式里的负号，直接写成 $\frac{\partial z}{\partial x}=\frac{F_x}{F_z}$，结果符号反了；二是求 $F_z$ 时把 $-4z$ 的导数漏掉，只写 $2z$，导致分母错误；三是没有把方程整理成 $F=0$ 的形式就直接求导，容易漏项；四是把 $F_x$ 求成 $2x+2z\frac{\partial z}{\partial x}$ 这种混合形式，那是直接对两边求导的做法，用公式法时 $F_x$ 必须把 $z$ 当常数。另外要留意题目给的 $z>2$ 条件，它保证 $F_z\neq 0$。

**【同类题识别技巧】**

以后看到"$F(x,y,z)=0$ 求 $\frac{\partial z}{\partial x}$"，无脑执行三步：移项写成 $F=0$、求 $F_x$ 与 $F_z$（$F_x$ 把 $z$ 当常数，$F_z$ 把 $x$ 当常数）、代入 $-\frac{F_x}{F_z}$。写完后检查一下自己的答案里是否含有负号，绝大多数隐函数求导的答案都带负号。

**【一句话总结】**

看到 $F(x,y,z)=0$ 求偏导 → 移项构造 $F$，算 $F_x$、$F_z$，代入 $-\frac{F_x}{F_z}$，别丢负号。

### 题 8.3-2　【变式】　难度 ★★　建议用时 9分钟　重要程度 ★★★★★

**知识点**：多元微分/隐函数

**【题目】**

设方程 $e^{z}-xyz=0$ 确定隐函数 $z=z(x,y)$，求 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$。（专项训练原创题）

**【考查知识点】**

含指数与乘积项的隐函数求导：求 $F_x$、$F_y$、$F_z$ 时都用乘积求导法则。

**【题型识别】**

题型识别：看到"方程中含 $xyz$ 这种三个变量相乘的项以及 $e^z$"这个特征 → 属于一元方程确定的隐函数求导题型 → 用"构造 $F(x,y,z)$、逐项求偏导（乘积项用乘积法则）、代入隐函数求导公式"的方法。

**【需要记住的公式】**

1. 隐函数求导公式：$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}$，$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}$
2. 指数函数求导：$(e^z)'=e^z$
3. 乘积求导法则：$(xyz)_x=yz$，$(xyz)_y=xz$，$(xyz)_z=xy$

**【解题思路】**

解题思路：令 $F(x,y,z)=e^{z}-xyz$。求 $F_x$ 时把 $y$、$z$ 都看成常数：$e^z$ 是常数项导数为 0，$-xyz$ 中 $-yz$ 是常数因子、$x$ 求导得 1，所以 $F_x=-yz$。同理 $F_y=-xz$。求 $F_z$ 时把 $x$、$y$ 看成常数：$e^z$ 求导得 $e^z$，$-xyz$ 中 $-xy$ 是常数因子、$z$ 求导得 1，所以 $F_z=e^z-xy$。代入公式后还可以利用原方程 $e^z=xyz$ 把指数换掉，得到更整洁的形式。

**【详细解答】**

第一步：把方程化为标准形式。原方程为 $e^{z}-xyz=0$，已经在一边了，直接令
$$F(x,y,z)=e^{z}-xyz$$

第二步：求 $F_x$。把 $y$、$z$ 都看成常数，对 $x$ 求导：
$e^{z}$ 中不含 $x$，它是常数项，导数为 0。
$-xyz$ 中 $-yz$ 是常数因子（$y$、$z$ 都当常数），$x$ 对 $x$ 求导得 1，所以这一项导数为 $-yz$。
相加得
$$F_x=-yz$$

第三步：求 $F_y$。把 $x$、$z$ 都看成常数，对 $y$ 求导：
$e^{z}$ 导数为 0。
$-xyz$ 中 $-xz$ 是常数因子，$y$ 求导得 1，所以这一项导数为 $-xz$。
相加得
$$F_y=-xz$$

第四步：求 $F_z$。把 $x$、$y$ 都看成常数，对 $z$ 求导：
$e^{z}$ 对 $z$ 求导得 $e^{z}$。
$-xyz$ 中 $-xy$ 是常数因子，$z$ 求导得 1，所以这一项导数为 $-xy$。
相加得
$$F_z=e^{z}-xy$$

第五步：代入隐函数求导公式。
$$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}=-\frac{-yz}{e^{z}-xy}=\frac{yz}{e^{z}-xy}$$
$$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}=-\frac{-xz}{e^{z}-xy}=\frac{xz}{e^{z}-xy}$$
两个负号相消，所以分子变成正的。

第六步：用原方程化简形式。由 $e^{z}=xyz$，把分母中的 $e^{z}$ 换成 $xyz$：
$$e^{z}-xy=xyz-xy=xy(z-1)$$
于是
$$\frac{\partial z}{\partial x}=\frac{yz}{xy(z-1)}=\frac{z}{x(z-1)}$$
$$\frac{\partial z}{\partial y}=\frac{xz}{xy(z-1)}=\frac{z}{y(z-1)}$$
在约分时用到了 $x\neq 0$、$y\neq 0$（由方程 $e^z=xyz$ 且 $e^z>0$ 可知 $xyz\neq 0$，所以 $x$、$y$、$z$ 都不为零）。

第七步：验算。用具体数值检查。取 $x=1$、$y=e$，则 $xyz=z e$，方程 $e^z=ze$ 在 $z=1$ 处成立（$e^1=e\cdot 1=e$），所以点 $(1,e,1)$ 在隐函数曲面上。公式给出 $\frac{\partial z}{\partial x}=\frac{z}{x(z-1)}$，代入 $z=1$ 得分母 $1\cdot(1-1)=0$，这时不能代入，说明该点处 $F_z=e^{z}-xy=e-1\cdot e=0$，隐函数定理的条件不满足，确实要避开。换一个点：取 $x=1$、$y=1$，方程变为 $e^z=z$，这个方程在实数范围内无解（因为 $e^z>z$ 对一切实数 $z$ 成立），说明这一点没有对应的隐函数值，也应当避开。再取 $x=2$、$y=1$，方程变为 $e^z=2z$：当 $z\geq 0$ 时 $e^z\geq ez>2z$，当 $z<0$ 时 $e^z>0>2z$，所以这个方程在实数范围内根本无解（一般地，$e^z=cz$ 只有当 $c>e$ 时才有正实解），这一点也应当避开。这里改用更直接的验证：对第五步的原始公式做恒等式检验，把 $z=z(x,y)$ 代回方程两边对 $x$ 求偏导：左边 $\frac{\partial}{\partial x}e^z=e^z\frac{\partial z}{\partial x}$，右边 $\frac{\partial}{\partial x}(xyz)=yz+xy\frac{\partial z}{\partial x}$，两边相等给出 $e^z\frac{\partial z}{\partial x}=yz+xy\frac{\partial z}{\partial x}$，移项得 $\frac{\partial z}{\partial x}(e^z-xy)=yz$，即 $\frac{\partial z}{\partial x}=\frac{yz}{e^z-xy}$，与第五步结果完全一致，答案可靠。对 $y$ 方向做同样的检验：把方程两边对 $y$ 求偏导得 $e^z\frac{\partial z}{\partial y}=xz+xy\frac{\partial z}{\partial y}$，移项得 $\frac{\partial z}{\partial y}(e^z-xy)=xz$，即 $\frac{\partial z}{\partial y}=\frac{xz}{e^z-xy}$，同样一致。

**【最终答案】**

$\frac{\partial z}{\partial x}=\frac{yz}{e^{z}-xy}=\frac{z}{x(z-1)}$，$\frac{\partial z}{\partial y}=\frac{xz}{e^{z}-xy}=\frac{z}{y(z-1)}$

**【易错点】**

常见错误：一是忘记公式中的负号，而本题分子本身还带一个负号（$F_x=-yz$），两个负号相消后结果为正，很多同学在这里把符号搞成负的；二是求 $F_z$ 时把 $e^z$ 的导数写成 $e^z\cdot 1$ 之外的多余因子，或者把 $-xyz$ 对 $z$ 的导数写成 $-xyz$；三是在化简时把 $e^z$ 换成 $xyz$ 之后没有提取公因式就直接约分；四是忽略 $x\neq 0$、$y\neq 0$、$F_z\neq 0$ 这些前提条件。另外要注意把 $z$ 视为 $x$、$y$ 的函数时，$e^z$ 的偏导是 $e^z\frac{\partial z}{\partial x}$，不能写成 0，这与用公式法求 $F_x$ 时的处理完全不同，两种方法不要混用。

**【同类题识别技巧】**

以后看到隐函数方程里含乘积项 $xyz$，先想"这个乘积对每个变量求偏导分别是多少"：对 $x$ 是 $yz$，对 $y$ 是 $xz$，对 $z$ 是 $xy$。把这三个结果写在草稿纸边上再套公式，可以避免漏项。凡是分子分母能借助原方程化简的，都化简成不含 $e^z$ 的形式，答案更整洁也更便于阅卷。

**【一句话总结】**

看到 $e^z-xyz=0$ 这类含乘积的隐函数 → 求 $F_x$、$F_y$、$F_z$，套 $-\frac{F_x}{F_z}$，再用原方程化简。

### 题 8.3-3　【变式】　难度 ★★　建议用时 7分钟　重要程度 ★★★★★

**知识点**：多元微分/隐函数

**【题目】**

设方程 $x^2+y^2+z^2=4z$ 确定隐函数 $z=z(x,y)$，求 $\frac{\partial^2 z}{\partial x\partial y}$ 在点 $x=0$、$y=0$、$z=4$ 处的值。（根据 CMC 常见题型改编）

**【考查知识点】**

隐函数的二阶混合偏导：把一阶偏导再对另一个变量求导，注意 $z$ 本身仍依赖于 $x$、$y$。

**【题型识别】**

题型识别：看到"先求隐函数的一阶偏导，再要求二阶混合偏导并在给定点求值"这个特征 → 属于隐函数高阶偏导题型 → 用"先求出一阶偏导的表达式、注意其中含 $z$、再对另一个变量求导（$z$ 还要按链式法则继续求导）、最后代入数值"的方法。

**【需要记住的公式】**

1. 隐函数一阶偏导：$\frac{\partial z}{\partial x}=-\frac{x}{z-2}$，$\frac{\partial z}{\partial y}=-\frac{y}{z-2}$
2. 商的求导法则：$\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$
3. 链式法则：$z$ 是 $x$、$y$ 的函数，所以 $\frac{\partial}{\partial y}(z-2)=\frac{\partial z}{\partial y}$

**【解题思路】**

解题思路：先由上一题的结果写出 $\frac{\partial z}{\partial x}=-\frac{x}{z-2}$。注意这个表达式里含有 $z$，而 $z$ 本身就是 $x$、$y$ 的函数，所以把它对 $y$ 求偏导时，不仅分子的 $x$ 是常数（对 $y$ 来说与它无关），分母 $z-2$ 还要按链式法则求导，得到 $\frac{\partial z}{\partial y}$。本题求的是在 $(x,y)=(0,0)$、$z=4$ 处的值，所以在求完导数表达式后，只要把 $z_y$ 在该点的值代入即可。另外可以先用对称性判断：函数 $F=x^2+y^2+z^2-4z$ 关于 $x$、$y$ 完全对称，且求值点 $x=0$、$y=0$ 在对称位置上，由此可以先猜 $\frac{\partial z}{\partial y}\big|_{(0,0)}=0$，进而 $\frac{\partial^2 z}{\partial x\partial y}\big|_{(0,0)}=0$，再严格算一遍验证。

**【详细解答】**

第一步：写出一阶偏导的表达式。由 $F(x,y,z)=x^2+y^2+z^2-4z$ 得 $F_x=2x$、$F_z=2z-4$，所以
$$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}=-\frac{2x}{2z-4}=-\frac{x}{z-2}$$

第二步：求 $\frac{\partial z}{\partial y}$ 在点 $(0,0)$（此时 $z=4$）处的值。先写出一般表达式：$F_y=2y$、$F_z=2z-4$，所以
$$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}=-\frac{2y}{2z-4}=-\frac{y}{z-2}$$
在点 $x=0$、$y=0$、$z=4$ 处代入得
$$\frac{\partial z}{\partial y}\bigg|_{(0,0)}=-\frac{0}{4-2}=0$$

第三步：把 $\frac{\partial z}{\partial x}$ 对 $y$ 求偏导。此时 $x$ 是常数（求的是对 $y$ 的偏导），而 $z$ 是 $y$ 的函数，所以要用商的求导法则。把 $-\frac{x}{z-2}$ 看成常数因子 $(-x)$ 乘以 $\frac{1}{z-2}$，或者直接对商求导：
$$\frac{\partial}{\partial y}\left(-\frac{x}{z-2}\right)=-x\cdot\frac{\partial}{\partial y}\left(\frac{1}{z-2}\right)$$
而 $\frac{\partial}{\partial y}\left(\frac{1}{z-2}\right)=-\frac{1}{(z-2)^2}\cdot\frac{\partial(z-2)}{\partial y}=-\frac{1}{(z-2)^2}\cdot\frac{\partial z}{\partial y}$。这里用到的是复合函数链式法则：因为 $z$ 依赖 $y$，所以 $(z-2)$ 也依赖 $y$，它的偏导就是 $\frac{\partial z}{\partial y}$。于是
$$\frac{\partial^2 z}{\partial x\partial y}=-x\cdot\left(-\frac{1}{(z-2)^2}\cdot\frac{\partial z}{\partial y}\right)=\frac{x}{(z-2)^2}\cdot\frac{\partial z}{\partial y}$$

第四步：代入数值。在点 $x=0$、$y=0$、$z=4$ 处，由第二步已经算出 $\frac{\partial z}{\partial y}\big|_{(0,0)}=0$，且 $x=0$、$(z-2)^2=(4-2)^2=4\neq 0$，所以
$$\frac{\partial^2 z}{\partial x\partial y}\bigg|_{(0,0)}=\frac{0}{4}\cdot 0=0$$

第五步：验算。用显式解验证。由 $z^2-4z+x^2+y^2=0$ 解得 $z=2+\sqrt{4-x^2-y^2}$（取 $z>2$ 这一支）。记 $w=\sqrt{4-x^2-y^2}$，则 $z=2+w$，且
$$\frac{\partial z}{\partial x}=-\frac{x}{w},\qquad \frac{\partial z}{\partial y}=-\frac{y}{w}$$
把这 $\frac{\partial z}{\partial x}$ 再对 $y$ 求偏导：$-\frac{x}{w}$ 中 $x$ 是常数因子，$\frac{1}{w}=w^{-1}$ 对 $y$ 求导得 $-w^{-2}\frac{\partial w}{\partial y}$，而 $w$ 对 $y$ 的偏导为 $-\frac{y}{w}$，所以
$$\frac{\partial^2 z}{\partial x\partial y}=-x\cdot\left(-w^{-2}\right)\cdot\left(-\frac{y}{w}\right)=-x\cdot\frac{1}{w^2}\cdot\frac{y}{w}=-\frac{xy}{w^3}$$
在 $x=0$、$y=0$ 处 $w=\sqrt{4}=2$，所以 $\frac{\partial^2 z}{\partial x\partial y}\big|_{(0,0)}=-\frac{0\cdot 0}{8}=0$，与前面的结果 0 完全一致。还可以做数值检查：在 $(0,0)$ 附近，$\frac{\partial z}{\partial x}=-\frac{x}{w}\approx-\frac{x}{2}$，它关于 $y$ 是偶函数（因为 $w$ 中只含 $y^2$），所以对 $y$ 的变化率在 $y=0$ 处为 0，与结论一致。答案可靠。

**【最终答案】**

$\frac{\partial^2 z}{\partial x\partial y}\bigg|_{(0,0,4)}=0$

**【易错点】**

最大的坑是把 $-\frac{x}{z-2}$ 对 $y$ 求导时把 $z$ 当成常数，直接写 $\frac{\partial}{\partial y}\left(-\frac{x}{z-2}\right)=0$。要牢记 $z$ 是 $x$、$y$ 的隐函数，凡是出现 $z$ 的地方对 $x$ 或 $y$ 求导都要再乘一个 $\frac{\partial z}{\partial x}$ 或 $\frac{\partial z}{\partial y}$。第二个坑是商求导时符号出错，把 $-\frac{1}{(z-2)^2}$ 写成 $+\frac{1}{(z-2)^2}$。第三个坑是代入数值时没有先算出该点的 $\frac{\partial z}{\partial y}$，就匆忙下结论。

**【同类题识别技巧】**

以后看到"隐函数的二阶偏导"，记住一句话：一阶偏导的表达式中含 $z$，所以再求一次导时 $z$ 还要导一次。写完答案后用显式解（能解出来就解出来）复核一遍，是最可靠的验算方式。如果求值点具有对称性（如本题的 $x=0$、$y=0$），可以先用对称性猜出答案再严格验证。

**【一句话总结】**

看到隐函数求二阶混合偏导 → 一阶偏导里的 $z$ 还要继续求导，最后代入具体点。

### 题 8.3-4　【变式】　难度 ★★　建议用时 8分钟　重要程度 ★★★★★

**知识点**：多元微分/隐函数

**【题目】**

设方程 $z^3-3xyz=a^3$（$a$ 为非零常数）确定隐函数 $z=z(x,y)$，求 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$。（专项训练原创题）

**【考查知识点】**

含常数项的隐函数求导：常数项求导后为零，但要把它写进 $F$ 中保持方程形式完整。

**【题型识别】**

题型识别：看到"方程中含 $z^3$ 与乘积项 $xyz$，还带有常数 $a^3$"这个特征 → 属于一元方程确定的隐函数求导题型 → 用"构造 $F(x,y,z)=z^3-3xyz-a^3$、求三个偏导、套隐函数求导公式"的方法。

**【需要记住的公式】**

1. 隐函数求导公式：$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}$，$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}$
2. 幂函数求导：$(z^3)'=3z^2$
3. 乘积项的偏导：$(xyz)_x=yz$，$(xyz)_z=xy$

**【解题思路】**

解题思路：先移项构造 $F(x,y,z)=z^3-3xyz-a^3$。求 $F_x$ 时把 $y$、$z$ 当常数：$z^3$ 与 $a^3$ 都是常数项导数为 0，$-3xyz$ 中 $-3yz$ 是常数因子、$x$ 求导得 1，所以 $F_x=-3yz$。同理 $F_y=-3xz$。求 $F_z$ 时把 $x$、$y$ 当常数：$z^3$ 求导得 $3z^2$，$-3xyz$ 中 $-3xy$ 是常数因子、$z$ 求导得 1，所以 $F_z=3z^2-3xy$。代入公式后两个负号相消，再把公因子 3 约去。

**【详细解答】**

第一步：移项构造函数。原方程为 $z^3-3xyz=a^3$，把右边的 $a^3$ 移到左边：
$$z^3-3xyz-a^3=0$$
令
$$F(x,y,z)=z^3-3xyz-a^3$$

第二步：求 $F_x$。把 $y$、$z$ 都看成常数：
$z^3$ 不含 $x$，导数为 0；$a^3$ 是常数，导数为 0；$-3xyz$ 中 $-3yz$ 是常数因子，$x$ 对 $x$ 求导得 1，所以这一项导数为 $-3yz$。于是
$$F_x=-3yz$$

第三步：求 $F_y$。把 $x$、$z$ 都看成常数：
$z^3$ 与 $a^3$ 导数为 0；$-3xyz$ 中 $-3xz$ 是常数因子，$y$ 求导得 1，所以这一项导数为 $-3xz$。于是
$$F_y=-3xz$$

第四步：求 $F_z$。把 $x$、$y$ 都看成常数：
$z^3$ 对 $z$ 求导得 $3z^2$；$a^3$ 导数为 0；$-3xyz$ 中 $-3xy$ 是常数因子，$z$ 求导得 1，所以这一项导数为 $-3xy$。于是
$$F_z=3z^2-3xy$$
把公因子 3 提出来写成 $F_z=3(z^2-xy)$。

第五步：代入隐函数求导公式。
$$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z}=-\frac{-3yz}{3z^2-3xy}=\frac{3yz}{3(z^2-xy)}=\frac{yz}{z^2-xy}$$
$$\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}=-\frac{-3xz}{3z^2-3xy}=\frac{3xz}{3(z^2-xy)}=\frac{xz}{z^2-xy}$$

第六步：验算。把方程两边直接对 $x$ 求偏导（把 $z$ 看作 $x$ 的函数）来复核。左边 $z^3$ 对 $x$ 求偏导得 $3z^2\frac{\partial z}{\partial x}$；$-3xyz$ 对 $x$ 求偏导得 $-3yz-3xy\frac{\partial z}{\partial x}$（用乘积法则，把 $y$ 当常数）；右边 $a^3$ 的偏导为 0。于是
$$3z^2\frac{\partial z}{\partial x}-3yz-3xy\frac{\partial z}{\partial x}=0$$
把含 $\frac{\partial z}{\partial x}$ 的项合并：
$$3\left(z^2-xy\right)\frac{\partial z}{\partial x}=3yz$$
两边同时除以 $3(z^2-xy)$（在 $z^2-xy\neq 0$ 的点上）得
$$\frac{\partial z}{\partial x}=\frac{yz}{z^2-xy}$$
与第五步结果完全一致。对 $y$ 方向做同样的检查：方程两边对 $y$ 求偏导得 $3z^2\frac{\partial z}{\partial y}-3xz-3xy\frac{\partial z}{\partial y}=0$，整理得 $\frac{\partial z}{\partial y}=\frac{xz}{z^2-xy}$，同样一致。再用一个具体数值检验：取 $a=1$、$x=0$、$y=0$，方程变成 $z^3=1$，取实根 $z=1$，此时公式给出 $\frac{\partial z}{\partial x}=\frac{0\cdot 1}{1-0}=0$、$\frac{\partial z}{\partial y}=0$，符合对称性。答案可靠。

**【最终答案】**

$\frac{\partial z}{\partial x}=\frac{yz}{z^2-xy}$，$\frac{\partial z}{\partial y}=\frac{xz}{z^2-xy}$

**【易错点】**

常见错误：一是忘记公式里的负号，本题 $F_x=-3yz$ 本身带负号，两个负号相消后结果为正，很多同学在这里多写了负号；二是求 $F_z$ 时把 $-3xyz$ 对 $z$ 的导数写成 $-3xyz$，忘记 $z$ 求导后只剩 1；三是把常数 $a^3$ 当作变量，写出 $3a^2\frac{\partial a}{\partial x}$ 这样的式子，要牢记 $a$ 是常数；四是约分时只约掉分子上的 3 而忘记分母也要约，导致系数错误。另外两个答案的分母完全相同，可以用这一点自查是否算错。

**【同类题识别技巧】**

以后看到"含 $z^3$ 或 $z^n$ 的隐函数方程"，套公式前先在草稿纸上写出三项：$F_x$（把 $y$、$z$ 当常数）、$F_y$（把 $x$、$z$ 当常数）、$F_z$（把 $x$、$y$ 当常数），三写清楚再代入。凡是被积表达式里出现 $xyz$ 这种对称的乘积项，两个答案往往呈对称形式（本题为 $\frac{yz}{z^2-xy}$ 与 $\frac{xz}{z^2-xy}$），可以用这个规律自查。

**【一句话总结】**

看到 $z^3-3xyz=a^3$ 求偏导 → 构造 $F$，算三个偏导，套 $-\frac{F_x}{F_z}$，两个负号相消。

### 题 8.3-5　【基础训练】　难度 ★★　建议用时 8分钟　重要程度 ★★★★★

**知识点**：多元微分/隐函数

**【题目】**

设方程组
$$\begin{cases} u+v=x \\ u^2+v^2=y \end{cases}$$
确定隐函数 $u=u(x,y)$、$v=v(x,y)$，求 $\frac{\partial u}{\partial x}$ 与 $\frac{\partial v}{\partial x}$。（根据 CMC 常见题型改编）

**【考查知识点】**

由方程组确定的隐函数：把两个方程同时对 $x$ 求偏导，解二元一次方程组得到两个偏导。

**【题型识别】**

题型识别：看到"两个方程确定两个隐函数 $u$、$v$，要求它们对 $x$ 的偏导"这个特征 → 属于方程组确定的隐函数求导题型 → 用"两个方程两边同时对 $x$ 求偏导（把 $y$ 当常数、$u$、$v$ 当 $x$ 的函数）、把 $\frac{\partial u}{\partial x}$ 与 $\frac{\partial v}{\partial x}$ 当未知数解方程组"的方法。

**【需要记住的公式】**

1. 方程两边对 $x$ 求偏导：$\frac{\partial}{\partial x}(u^2)=2u\frac{\partial u}{\partial x}$
2. 二元一次方程组解法：$\begin{cases} a_1p+b_1q=c_1 \\ a_2p+b_2q=c_2 \end{cases}$ 用消元法或克拉默法则解出 $p$、$q$
3. 平方项化简：$u^2+v^2=(u+v)^2-2uv$

**【解题思路】**

解题思路：本题有两个未知函数 $u$、$v$，所以不能套单方程的那个公式，正确做法是把两个方程的两边同时对 $x$ 求偏导。求偏导时把 $y$ 看成常数，而 $u$、$v$ 都是 $x$ 的函数，所以对 $u^2$ 求偏导要用链式法则得 $2u\frac{\partial u}{\partial x}$。这样得到两个方程，其中 $\frac{\partial u}{\partial x}$ 与 $\frac{\partial v}{\partial x}$ 是未知数，$u$、$v$ 已知，就是一个二元一次方程组，解出来即可。另外可以用 $u+v=x$ 得到一个捷径：把这个方程两边对 $x$ 求偏导立刻得到 $\frac{\partial u}{\partial x}+\frac{\partial v}{\partial x}=1$，再用第二个方程求出两者的差，就可以分别解出它们。

**【详细解答】**

第一步：把第一个方程两边同时对 $x$ 求偏导（把 $y$ 看成常数，$u$、$v$ 看成 $x$ 的函数）。
$$u+v=x\quad\Rightarrow\quad \frac{\partial u}{\partial x}+\frac{\partial v}{\partial x}=1$$
这里左边两项都含 $x$，都要用链式法则，$u$ 对 $x$ 的偏导就是 $\frac{\partial u}{\partial x}$，$v$ 对 $x$ 的偏导就是 $\frac{\partial v}{\partial x}$；右边 $x$ 对 $x$ 求偏导得 1。

第二步：把第二个方程两边同时对 $x$ 求偏导。
$$u^2+v^2=y\quad\Rightarrow\quad 2u\frac{\partial u}{\partial x}+2v\frac{\partial v}{\partial x}=0$$
左边 $u^2$ 对 $x$ 求偏导要用链式法则：外层 $2u$，内层 $\frac{\partial u}{\partial x}$，所以得 $2u\frac{\partial u}{\partial x}$；$v^2$ 同理得 $2v\frac{\partial v}{\partial x}$。右边 $y$ 对 $x$ 求偏导时 $y$ 是常数，得 0。

第二步的式子两边同时除以 2，化简得
$$u\frac{\partial u}{\partial x}+v\frac{\partial v}{\partial x}=0$$

第三步：把两个化简后的方程联立，记 $p=\frac{\partial u}{\partial x}$、$q=\frac{\partial v}{\partial x}$，得到
$$\begin{cases} p+q=1 \\ up+vq=0 \end{cases}$$

第四步：解这个二元一次方程组。由第一个方程得 $p=1-q$，代入第二个方程：
$$u(1-q)+vq=0$$
展开得
$$u-uq+vq=0$$
把含 $q$ 的项合并：
$$q(v-u)=-u$$
所以当 $v\neq u$ 时
$$q=\frac{-u}{v-u}=\frac{u}{u-v}$$
再代回 $p=1-q$：
$$p=1-\frac{u}{u-v}=\frac{u-v-u}{u-v}=\frac{-v}{u-v}=\frac{v}{v-u}$$

第五步：写出结论。
$$\frac{\partial u}{\partial x}=\frac{v}{v-u},\qquad \frac{\partial v}{\partial x}=\frac{u}{u-v}$$
这两个表达式在形式上正好相差一个负号，可以互相核对：第一步的方程要求 $p+q=1$，而这两个答案之和为 $\frac{v}{v-u}+\frac{u}{u-v}=\frac{v}{v-u}-\frac{u}{v-u}=\frac{v-u}{v-u}=1$，正好与第一步的方程 $p+q=1$ 相符。

第六步：验算。用具体数值检查。取 $x=0$、$y=1$，则方程组变成 $u+v=0$、$u^2+v^2=1$，由 $v=-u$ 代入得 $u^2+u^2=1$，即 $u^2=\frac12$，取 $u=\frac{\sqrt{2}}{2}$、$v=-\frac{\sqrt{2}}{2}$。公式给出
$$\frac{\partial u}{\partial x}=\frac{v}{v-u}=\frac{-\frac{\sqrt{2}}{2}}{-\frac{\sqrt{2}}{2}-\frac{\sqrt{2}}{2}}=\frac{-\frac{\sqrt{2}}{2}}{-\sqrt{2}}=\frac12$$
$$\frac{\partial v}{\partial x}=\frac{u}{u-v}=\frac{\frac{\sqrt{2}}{2}}{\sqrt{2}}=\frac12$$
两个偏导都是 $\frac12$，它们的和为 1，与第一步的方程 $p+q=1$ 一致。再用数值微分检验：取 $x=0.001$、$y=1$，方程组为 $u+v=0.001$、$u^2+v^2=1$。由第一个方程 $v=0.001-u$，代入第二个方程得 $u^2+(0.001-u)^2=1$，即 $2u^2-0.002u+0.000001-1=0$，即 $2u^2-0.002u-0.999999=0$，解出 $u=\frac{0.002+\sqrt{0.000004+7.999992}}{4}=\frac{0.002+\sqrt{7.999996}}{4}$。而 $\sqrt{7.999996}=2.8284269$（因为 $\sqrt{8}=2.8284271$），所以 $u\approx\frac{0.002+2.8284269}{4}=\frac{2.8304269}{4}=0.7076067$。原来的 $u=0.7071068$，变化量约为 $0.0005$，除以 $\Delta x=0.001$ 得约 $0.5$，与公式结果 $\frac12$ 一致。答案可靠。

**【最终答案】**

$\frac{\partial u}{\partial x}=\frac{v}{v-u}$，$\frac{\partial v}{\partial x}=\frac{u}{u-v}$

**【易错点】**

常见错误：一是把第二个方程对 $x$ 求偏导时只写 $2u$、忘记乘上内层的 $\frac{\partial u}{\partial x}$，这是链式法则的典型漏乘；二是把右边 $y$ 的偏导写成 1，$y$ 对 $x$ 求偏导时 $y$ 是常数，应当得 0；三是解方程组时漏掉一个未知数，只求出 $\frac{\partial u}{\partial x}$ 就交卷；四是没有注意 $v\neq u$ 这个前提，当 $v=u$ 时系数行列式为零，要单独讨论。另外两个答案的分母一个是 $v-u$、一个是 $u-v$，写的时候容易互换，建议最后用 $p+q=1$ 自查一遍。

**【同类题识别技巧】**

以后看到"方程组确定多个隐函数"，一律对每个方程的两边同时求偏导，得到一个"未知数个数等于方程个数"的线性方程组，再解它。解完后一定要用"把两个答案代回原方程是否成立"来验算，这是最快的自查方法。

**【一句话总结】**

看到方程组确定隐函数求偏导 → 每个方程两边同时对自变量求偏导，把待求偏导当未知数解方程组。

## 8.4 题型四 空间曲线的切线与曲面的切平面

> **这一类题我到底应该记住什么？**
>
> 这一类题问的都是"切线、法线、切平面、法平面"，做法只有一个核心动作：先找出一个向量。四条口诀：① 空间曲线由参数式 $x(t),y(t),z(t)$ 给出，切向量就是 $(x',y',z')$；② 曲面由 $F(x,y,z)=0$ 给出，法向量就是对 $F$ 求梯度 $\nabla F=(F_x,F_y,F_z)$；③ 曲面由 $z=f(x,y)$ 给出，法向量是 $(-f_x,-f_y,1)$，等价写法是切平面 $z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$；④ 两个曲面相交成的曲线，切向量等于两个法向量的叉乘。另外不管哪种情形，第一步都要把给定的点代回原方程，确认这个点确实在曲线或曲面上。

### 题 8.4-1　【母题】　难度 ★★　建议用时 6分钟　重要程度 ★★★★★

**知识点**：多元微分/空间曲线切线

**【题目】**

已知空间曲线 $\Gamma$ 的参数方程为 $x=t^2$，$y=2t$，$z=t^3$，求 $\Gamma$ 在 $t=1$ 所对应的点处的切线方程与法平面方程。（专项训练原创题）

**【考查知识点】**

参数方程给出的空间曲线的切向量，以及由切向量写出的切线方程与法平面方程。

**【题型识别】**

看到曲线用参数 $t$ 的方程 $x=x(t),y=y(t),z=z(t)$ 给出，问切线或法平面 → 属于"参数式空间曲线求切线"的题型 → 先求切点，再把三个坐标分别对 $t$ 求导得到切向量，最后套点向式直线与点法式平面公式。

**【需要记住的公式】**

1. 曲线 $x=x(t),y=y(t),z=z(t)$ 在 $t=t_0$ 处的切向量为 $\vec{T}=(x'(t_0),y'(t_0),z'(t_0))$
2. 过点 $(x_0,y_0,z_0)$、方向向量为 $(A,B,C)$ 的直线：$\frac{x-x_0}{A}=\frac{y-y_0}{B}=\frac{z-z_0}{C}$
3. 以 $(A,B,C)$ 为法向量、过点 $(x_0,y_0,z_0)$ 的平面：$A(x-x_0)+B(y-y_0)+C(z-z_0)=0$

**【解题思路】**

切线是"拿切向量当直线的方向向量"，法平面是"拿同一个切向量当平面的法向量"。所以整道题只要求出一个量：切向量。参数形式求切向量最省事，直接把三个坐标对参数求导，不必消去参数，也不必去算 $dy/dx$。

**【详细解答】**

第一步，求切点。把 $t=1$ 代入参数方程，三个坐标分别算出来：
$$x=1^2=1,\quad y=2\times 1=2,\quad z=1^3=1$$
所以切点为 $P(1,2,1)$。

第二步，求切向量。三个坐标分别对 $t$ 求导，用的是基本求导公式：
$$x'(t)=2t,\quad y'(t)=2,\quad z'(t)=3t^2$$
把 $t=1$ 代入这三个导数：
$$x'(1)=2,\quad y'(1)=2,\quad z'(1)=3$$
所以切向量为 $\vec{T}=(2,2,3)$。

第三步，写切线方程。以 $\vec{T}=(2,2,3)$ 为方向向量，直线过点 $P(1,2,1)$，代入点向式公式得
$$\frac{x-1}{2}=\frac{y-2}{2}=\frac{z-1}{3}$$

第四步，写法平面方程。法平面就是"以切向量为法向量、过切点"的平面：
$$2(x-1)+2(y-2)+3(z-1)=0$$
把括号逐项展开：$2x-2+2y-4+3z-3=0$，合并常数项得 $2x+2y+3z-9=0$，也就是 $2x+2y+3z=9$。

第五步，验算。验点：把 $P(1,2,1)$ 代入 $2x+2y+3z$，得 $2+4+3=9$，与常数项 $9$ 一致，切点在法平面上。验方向：法平面的法向量是 $(2,2,3)$，切线的方向向量也是 $(2,2,3)$，两者相同，说明切线确实垂直于法平面，这正是法平面的定义要求。

**【最终答案】**

切线：$\frac{x-1}{2}=\frac{y-2}{2}=\frac{z-1}{3}$；法平面：$2x+2y+3z=9$

**【易错点】**

最容易错的是把 $t=1$ 直接当成切点坐标，写成 $(1,1,1)$ 之类；切点的三个坐标必须把 $t=1$ 代回原来的参数方程分别算。第二个高频错误是求导：$z=t^3$ 的导数是 $3t^2$，在 $t=1$ 处是 $3$，漏掉平方会写成 $3$ 之外的错误值。第三，切线方程的分母是切向量的三个分量，分子是 $x-x_0$ 型的差，符号不要写反。

**【同类题识别技巧】**

以后看到"曲线写成 $x(t),y(t),z(t)$ 的形式，求切线或法平面"，固定三步：代 $t_0$ 求点、求导求切向量、套公式写直线与平面。如果曲线是用两个曲面方程联立给出的，就换成"两个法向量叉乘"的办法，见本节的变式题。

**【一句话总结】**

看到参数式空间曲线求切线 → 切向量就是 $(x'(t_0),y'(t_0),z'(t_0))$ → 切线用它当方向向量，法平面用它当法向量。

### 题 8.4-2　【变式】　难度 ★★　建议用时 7分钟　重要程度 ★★★★★

**知识点**：多元微分/切平面

**【题目】**

求曲面 $x^2+2y^2+z^2=10$ 在点 $P(1,-2,1)$ 处的切平面方程与法线方程。（专项训练原创题）

**【考查知识点】**

$F(x,y,z)=0$ 型曲面的法向量（梯度）以及切平面、法线方程。

**【题型识别】**

看到曲面由含 $x,y,z$ 的三元方程给出（没有解出 $z$），问切平面或法线 → 属于 $F(x,y,z)=0$ 型曲面求切平面 → 先把方程移项成 $F(x,y,z)=0$，再求梯度 $\nabla F$ 得到法向量。

**【需要记住的公式】**

1. 曲面 $F(x,y,z)=0$ 在点 $P$ 处的法向量为 $\vec{n}=\nabla F(P)=(F_x(P),F_y(P),F_z(P))$
2. 切平面：$F_x(P)(x-x_0)+F_y(P)(y-y_0)+F_z(P)(z-z_0)=0$
3. 法线：$\frac{x-x_0}{F_x(P)}=\frac{y-y_0}{F_y(P)}=\frac{z-z_0}{F_z(P)}$

**【解题思路】**

"法向量怎么来"这个问题在这一类题里的答案很固定：把曲面写成 $F(x,y,z)=0$ 这种等值面形式，等值面的法向量就是梯度 $\nabla F$，也就是对 $F$ 分别求三个偏导数再代点。算出法向量以后，切平面用点法式，法线用点向式。

**【详细解答】**

第一步，把曲面写成等值面形式。把右边的 $10$ 移到左边，令
$$F(x,y,z)=x^2+2y^2+z^2-10$$
于是曲面就是方程 $F(x,y,z)=0$ 描述的等值面。

第二步，检验点 $P$ 在曲面上。把 $P(1,-2,1)$ 代入 $F$：
$$F(1,-2,1)=1^2+2\times(-2)^2+1^2-10=1+8+1-10=0$$
结果为 $0$，所以 $P$ 确实在曲面上，可以在这个点求切平面。

第三步，求法向量。对 $F$ 分别求三个偏导数，求 $F_x$ 时把 $y,z$ 看成常数，求 $F_y$ 时把 $x,z$ 看成常数，求 $F_z$ 时把 $x,y$ 看成常数：
$$F_x=2x,\quad F_y=4y,\quad F_z=2z$$
在 $P(1,-2,1)$ 处代入：
$$F_x(P)=2\times 1=2,\quad F_y(P)=4\times(-2)=-8,\quad F_z(P)=2\times 1=2$$
所以法向量 $\vec{n}=(2,-8,2)$。三个分量有公因子 $2$，约去后得 $\vec{n}=(1,-4,1)$，两个写法对应的法线是同一条直线。

第四步，写切平面方程。以 $\vec{n}=(1,-4,1)$ 为法向量，平面过 $P(1,-2,1)$，注意 $y-y_0=y-(-2)=y+2$：
$$1\cdot(x-1)-4\cdot(y+2)+1\cdot(z-1)=0$$
展开：$x-1-4y-8+z-1=0$，合并常数得 $x-4y+z-10=0$，即
$$x-4y+z=10$$

第五步，写法线方程。以 $\vec{n}=(1,-4,1)$ 为方向向量，直线过 $P$：
$$\frac{x-1}{1}=\frac{y+2}{-4}=\frac{z-1}{1}$$

第六步，验算。验点：把 $P$ 代入切平面左边，$1-4\times(-2)+1=1+8+1=10$，与右边的 $10$ 一致。验法向量：切平面的法向量 $(1,-4,1)$ 与 $\nabla F(P)=(2,-8,2)$ 成比例，符合推导。验方向：法线的方向向量 $(1,-4,1)$ 与切平面法向量相同，说明法线垂直于切平面。

**【最终答案】**

切平面：$x-4y+z=10$；法线：$\frac{x-1}{1}=\frac{y+2}{-4}=\frac{z-1}{1}$

**【易错点】**

第一，切平面公式里是 $(y-y_0)$，本题 $y_0=-2$，所以必须写成 $y+2$，写成 $y-2$ 是高频失分点，验算时用切点代回就能立刻发现。第二，$F_y=4y$ 在 $y=-2$ 处是 $-8$，负号不能丢。第三，求切平面前一定要验一次点在不在曲面上，如果点不在曲面上，这道题的提法本身就不成立，硬套公式必然错。

**【同类题识别技巧】**

以后看到曲面方程同时含 $x,y,z$、又不能方便地解出 $z$，就先设 $F=$ 左边减右边，用 $\nabla F$ 当法向量。这个办法对球面、椭球面、双曲面、柱面都通用。

**【一句话总结】**

看到曲面是三元方程 → 令 $F=$ 左边减右边 → 法向量 $\vec{n}=\nabla F(P)$ → 切平面用点法式、法线用点向式。

### 题 8.4-3　【变式】　难度 ★★　建议用时 6分钟　重要程度 ★★★★★

**知识点**：多元微分/切平面

**【题目】**

求曲面 $z=x^2+2y^2$ 在点 $P(1,1,3)$ 处的切平面方程。（专项训练原创题）

**【考查知识点】**

$z=f(x,y)$ 型曲面的法向量与切平面方程，以及它与 $F(x,y,z)=0$ 型写法的关系。

**【题型识别】**

看到曲面已经解成 $z=f(x,y)$ 的形式（右边只含 $x,y$），问切平面 → 属于 $z=f(x,y)$ 型曲面求切平面 → 先求两个偏导 $f_x,f_y$，再用公式 $z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$，或者设 $F=z-f(x,y)$ 用梯度求法向量。

**【需要记住的公式】**

1. 曲面 $z=f(x,y)$ 在 $(x_0,y_0)$ 处的法向量：$\vec{n}=(-f_x(x_0,y_0),-f_y(x_0,y_0),1)$
2. 切平面：$z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$
3. 偏导公式：$(x^2)_x=2x$，$(2y^2)_y=4y$

**【解题思路】**

"法向量怎么来"：把方程移项写成 $F(x,y,z)=z-x^2-2y^2=0$，它属于 $z-f(x,y)=0$ 的形状，对它求梯度时 $F_z=1$、$F_x=-f_x$、$F_y=-f_y$，于是 $\vec{n}=(-f_x,-f_y,1)$。所以两条路是同一件事：先算 $f_x,f_y$，再代点，最后写平面。先用简单公式算出切平面，再用梯度法核对法向量，心里更踏实。

**【详细解答】**

第一步，验证切点。$P(1,1,3)$ 的竖坐标是 $z_0=3$，而右边函数在 $(1,1)$ 处的值是 $f(1,1)=1^2+2\times 1^2=3$，两者相等，所以 $P$ 在曲面上。

第二步，求偏导数。对 $x$ 求偏导时把 $y$ 看成常数：$f_x(x,y)=2x$；对 $y$ 求偏导时把 $x$ 看成常数：$f_y(x,y)=4y$。在 $(1,1)$ 处代入：
$$f_x(1,1)=2\times 1=2,\quad f_y(1,1)=4\times 1=4$$

第三步，用切平面公式。以 $(x_0,y_0,z_0)=(1,1,3)$ 代入：
$$z-3=2\cdot(x-1)+4\cdot(y-1)$$
展开右边：$2x-2+4y-4=2x+4y-6$，所以 $z-3=2x+4y-6$，即
$$z=2x+4y-3$$

第四步，用梯度法核对。令 $F(x,y,z)=z-x^2-2y^2$，求三个偏导：$F_x=-2x$，$F_y=-4y$，$F_z=1$。在 $P(1,1,3)$ 处得 $\vec{n}=(-2,-4,1)$。以这个法向量、过 $P$ 写点法式平面：
$$-2(x-1)-4(y-1)+1\cdot(z-3)=0$$
展开：$-2x+2-4y+4+z-3=0$，即 $z=2x+4y-3$，与第三步完全相同，说明两种算法互相印证。

第五步，验算。把 $(x,y)=(1,1)$ 代回 $z=2x+4y-3$ 得 $z=2+4-3=3$，与切点竖坐标一致。再固定 $y=1$ 看这平面与平面 $y=1$ 的交线：$z=2x+1$，斜率是 $2$，正好等于 $f_x(1,1)=2$；固定 $x=1$ 时 $z=4y-1$，斜率是 $4$，正好等于 $f_y(1,1)=4$。两个斜率都对上，答案正确。

**【最终答案】**

$z=2x+4y-3$

**【易错点】**

第一，符号陷阱：切平面公式右边是 $+f_x(x-x_0)+f_y(y-y_0)$，而梯度法给出的法向量是 $(-f_x,-f_y,1)$，两者差一个负号，不能把公式和法向量混着写。第二，别忘了先验切点是否在曲面上。第三，$f_y$ 是对 $y$ 求导，$2y^2$ 的导数是 $4y$，在 $(1,1)$ 处是 $4$，写成 $2$ 会让整个平面错误。

**【同类题识别技巧】**

以后看到曲面已经写成 $z=f(x,y)$，优先用现成公式 $z-z_0=f_x(x-x_0)+f_y(y-y_0)$，一步到位；需要写切平面法向量或法线时，再换成 $\vec{n}=(-f_x,-f_y,1)$。这两套写法必须都会，因为填空题可能直接问法向量。

**【一句话总结】**

看到 $z=f(x,y)$ 求切平面 → 先算 $f_x,f_y$ → 用 $z-z_0=f_x(x-x_0)+f_y(y-y_0)$；要法向量就写 $(-f_x,-f_y,1)$。

### 题 8.4-4　【变式】　难度 ★★　建议用时 8分钟　重要程度 ★★★★★

**知识点**：多元微分/空间曲线切线

**【题目】**

曲线 $\Gamma$ 是曲面 $x^2+y^2+z^2=6$ 与曲面 $x+y+z=0$ 的交线，求 $\Gamma$ 在点 $P(1,-2,1)$ 处的切线方程。（根据 CMC 常见题型改编）

**【考查知识点】**

由两个曲面方程联立给出的空间曲线，其切向量等于两个曲面法向量的叉乘。

**【题型识别】**

看到曲线用两个曲面方程联立（通常写成 $\begin{cases} x^2+y^2+z^2=6 \\ x+y+z=0 \end{cases}$）给出，问切线 → 属于"两曲面交线求切线"的题型 → 分别求两个曲面的法向量，再做叉乘得到切向量。

**【需要记住的公式】**

1. 曲面 $F(x,y,z)=0$ 的法向量 $\vec{n}=\nabla F(P)=(F_x,F_y,F_z)$ 在 $P$ 点的值
2. 交线的切向量 $\vec{T}=\vec{n}_1\times\vec{n}_2$
3. 叉乘公式：$(a_1,a_2,a_3)\times(b_1,b_2,b_3)=(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1)$

**【解题思路】**

交线在两个曲面上，所以交线在 $P$ 点的切向量既垂直于第一个曲面的法向量，又垂直于第二个曲面的法向量。同时垂直于两个向量的向量就是它们的叉乘，于是 $\vec{T}=\vec{n}_1\times\vec{n}_2$。求出切向量后，切线就是过 $P$、以 $\vec{T}$ 为方向向量的直线。

**【详细解答】**

第一步，检验 $P$ 在交线上，也就是同时满足两个曲面方程。代入第一个方程：
$$1^2+(-2)^2+1^2=1+4+1=6$$
与右边的 $6$ 相等；代入第二个方程：$1+(-2)+1=0$，与右边的 $0$ 相等。所以 $P$ 确实在 $\Gamma$ 上。

第二步，求第一个曲面的法向量。令 $F_1=x^2+y^2+z^2-6$，求三个偏导：
$$(F_1)_x=2x,\quad (F_1)_y=2y,\quad (F_1)_z=2z$$
在 $P(1,-2,1)$ 处代入得 $\vec{n}_1=(2,-4,2)$。

第三步，求第二个曲面的法向量。令 $F_2=x+y+z$，三个偏导分别是 $1,1,1$，所以在 $P$ 点
$$\vec{n}_2=(1,1,1)$$

第四步，叉乘求切向量。按叉乘公式，第一个分量是"第二个和第三个分量交叉相乘再相减"：
$$T_1=(-4)\times 1-2\times 1=-4-2=-6$$
第二个分量是"第三个和第一个分量交叉相减"，注意公式里这一项前面带负号：
$$T_2=2\times 1-2\times 1=2-2=0$$
第三个分量是"第一个和第二个分量交叉相减"：
$$T_3=2\times 1-(-4)\times 1=2+4=6$$
所以 $\vec{T}=(-6,0,6)$，三个分量有公因子 $6$，约去后取 $\vec{T}=(-1,0,1)$。

第五步，写切线方程。直线过 $P(1,-2,1)$，方向向量为 $(-1,0,1)$：
$$\frac{x-1}{-1}=\frac{y+2}{0}=\frac{z-1}{1}$$
其中分母为 $0$ 的意思是分子必须为 $0$，即 $y+2=0$。所以这条切线也可以写成两个平面的交线：
$$\begin{cases} y=-2 \\ x+z=2 \end{cases}$$

第六步，验算。验垂直：$\vec{T}=(-1,0,1)$ 与 $\vec{n}_1=(2,-4,2)$ 的点积是 $(-1)\times 2+0\times(-4)+1\times 2=-2+2=0$，垂直；与 $\vec{n}_2=(1,1,1)$ 的点积是 $-1+0+1=0$，也垂直。验点：$P(1,-2,1)$ 满足 $y=-2$ 与 $x+z=1+1=2$，在切线上。

**【最终答案】**

$\frac{x-1}{-1}=\frac{y+2}{0}=\frac{z-1}{1}$，也写作 $\begin{cases} y=-2 \\ x+z=2 \end{cases}$

**【易错点】**

第一，把两个法向量相加或相减当成切向量，这是概念错误，必须是叉乘。第二，$F_2=x+y+z$ 的法向量是 $(1,1,1)$，不需要解出 $z$ 再求偏导。第三，叉乘的顺序会改变正负号：$\vec{n}_1\times\vec{n}_2$ 与 $\vec{n}_2\times\vec{n}_1$ 差一个负号，作为切线方向向量两者都对（直线相同），但过程要写清用的是哪一个。第四，方向向量有 $0$ 分量时不要以为方程无意义，分母为 $0$ 表示该方向分量是 $0$。

**【同类题识别技巧】**

以后看到曲线写成两个曲面方程联立，就立刻想"两个法向量叉乘"。求法向量时两个曲面都用 $\nabla F$，其中线性方程（如平面 $x+y+z=0$）的法向量就是它三个系数。

**【一句话总结】**

看到两曲面交线求切线 → 两个曲面各求 $\nabla F$ → 切向量 $=\vec{n}_1\times\vec{n}_2$ → 过交点写点向式。

### 题 8.4-5　【基础训练】　难度 ★★　建议用时 5分钟　重要程度 ★★★★

**知识点**：多元微分/切平面

**【题目】**

求球面 $x^2+y^2+z^2=14$ 在点 $P(1,2,3)$ 处的切平面方程。（专项训练原创题）

**【考查知识点】**

用梯度求球面的法向量，写出切平面方程。

**【题型识别】**

看到曲面是含 $x^2+y^2+z^2$ 的三元方程、问切平面 → 属于 $F(x,y,z)=0$ 型曲面求切平面 → 令 $F=$ 左边减右边，用 $\nabla F$ 当法向量，写点法式平面。

**【需要记住的公式】**

1. 曲面 $F(x,y,z)=0$ 在 $P$ 处的法向量 $\vec{n}=\nabla F(P)$
2. 切平面：$F_x(P)(x-x_0)+F_y(P)(y-y_0)+F_z(P)(z-z_0)=0$
3. 球面 $x^2+y^2+z^2=R^2$ 上一点 $(x_0,y_0,z_0)$ 处的切平面为 $x_0x+y_0y+z_0z=R^2$

**【解题思路】**

方法和前面一样：把常数移到左边得到 $F$，对它求梯度得法向量，再写点法式。这道题是标准基础题，算完以后可以用球面的现成结论 $x_0x+y_0y+z_0z=R^2$ 对答案做检查。

**【详细解答】**

第一步，检验切点。令 $F(x,y,z)=x^2+y^2+z^2-14$，把 $P(1,2,3)$ 代入：
$$F(1,2,3)=1^2+2^2+3^2-14=1+4+9-14=0$$
所以 $P$ 在球面上。

第二步，求法向量。对 $F$ 求三个偏导：$F_x=2x$，$F_y=2y$，$F_z=2z$。在 $P(1,2,3)$ 处代入：
$$F_x(P)=2,\quad F_y(P)=4,\quad F_z(P)=6$$
法向量 $\vec{n}=(2,4,6)$，各分量有公因子 $2$，约去后取 $\vec{n}=(1,2,3)$。

第三步，写切平面方程。以 $\vec{n}=(1,2,3)$ 为法向量，平面过 $P(1,2,3)$：
$$1\cdot(x-1)+2\cdot(y-2)+3\cdot(z-3)=0$$
逐项展开：$x-1+2y-4+3z-9=0$，合并常数得 $x+2y+3z-14=0$，即
$$x+2y+3z=14$$

第四步，验算。用球面的现成结论检验：球面 $x^2+y^2+z^2=R^2$ 上点 $(x_0,y_0,z_0)$ 处的切平面是 $x_0x+y_0y+z_0z=R^2$。这里 $(x_0,y_0,z_0)=(1,2,3)$、$R^2=14$，得到 $x+2y+3z=14$，与第三步一致。再验点：$1+2\times 2+3\times 3=1+4+9=14$，切点在切平面上。

**【最终答案】**

$x+2y+3z=14$

**【易错点】**

第一，法向量是 $(2x,2y,2z)$ 代点后的 $(2,4,6)$，不要漏乘系数 $2$ 之后又在展开时把 $(2,4,6)$ 和 $(1,2,3)$ 混用两次，两个写法只能选一个。第二，切平面公式中 $y-y_0$ 与 $z-z_0$ 的减号不能丢。第三，常数项合并容易算错：$1+4+9=14$，$R^2$ 也是 $14$，看起来像巧合，其实是切点在三坐标都取正且满足球面方程的正常结果，不要因此怀疑答案为 $0$。

**【同类题识别技巧】**

以后遇到球面、椭球面求切平面，都用 $\nabla F$ 三步走：移项、求梯度、写点法式。球面题还可以用 $x_0x+y_0y+z_0z=R^2$ 秒验答案。

**【一句话总结】**

看到球面或椭球面求切平面 → 移项成 $F=0$ → 法向量 $\nabla F(P)$ → 点法式写平面，再用现成结论验一下。

### 题 8.4-6　【提高训练】　难度 ★★★　建议用时 10分钟　重要程度 ★★★★

**知识点**：多元微分/切平面

**【题目】**

求椭球面 $x^2+2y^2+3z^2=21$ 上平行于平面 $x+4y+6z=0$ 的切平面方程。（根据 CMC 常见题型改编）

**【考查知识点】**

用"切平面的法向量与已知平面平行"列方程反求切点，再写切平面。

**【题型识别】**

看到题目说"求曲面上平行于某已知平面的切平面"，却没有给出切点 → 属于"未知切点、用平行条件反求切点"的题型 → 设切点为 $(x_0,y_0,z_0)$，让 $\nabla F(x_0,y_0,z_0)$ 与已知平面的法向量成比例，再配合切点在曲面上解出切点。

**【需要记住的公式】**

1. 曲面 $F(x,y,z)=0$ 在点 $(x_0,y_0,z_0)$ 处的法向量 $\vec{n}=(F_x,F_y,F_z)$ 在该点的值
2. 两平面平行 $\Leftrightarrow$ 两法向量成比例：$(A_1,B_1,C_1)=\lambda(A_2,B_2,C_2)$
3. 切平面：$F_x(x-x_0)+F_y(y-y_0)+F_z(z-z_0)=0$

**【解题思路】**

切平面平行于已知平面，等价于它们的法向量平行；而切平面的法向量就是椭球面的梯度。于是把"梯度与 $(1,4,6)$ 成比例"写成方程组，把切点的三个坐标都用同一个参数 $\lambda$ 表示，再代回椭球面方程求出 $\lambda$。要注意的是：平行的切平面一般有两个（椭球面的两侧各一个），两个都要保留。

**【详细解答】**

第一步，设切点并写出法向量。设切点为 $Q(x_0,y_0,z_0)$，令
$$F(x,y,z)=x^2+2y^2+3z^2-21$$
求三个偏导得 $F_x=2x$，$F_y=4y$，$F_z=6z$，所以在 $Q$ 点
$$\vec{n}=(2x_0,4y_0,6z_0)$$

第二步，用平行条件列出关系式。已知平面 $x+4y+6z=0$ 的法向量是 $(1,4,6)$。切平面与它平行，说明两个法向量成比例，即存在实数 $\lambda$ 使
$$(2x_0,4y_0,6z_0)=\lambda(1,4,6)$$
比较三个分量：
$$2x_0=\lambda,\quad 4y_0=4\lambda,\quad 6z_0=6\lambda$$
于是
$$x_0=\frac{\lambda}{2},\quad y_0=\lambda,\quad z_0=\lambda$$

第三步，用切点在椭球面上求出 $\lambda$。把上面三个表达式代入 $x^2+2y^2+3z^2=21$：
$$\left(\frac{\lambda}{2}\right)^2+2\lambda^2+3\lambda^2=21$$
左边合并：$\frac{\lambda^2}{4}+2\lambda^2+3\lambda^2=\frac{\lambda^2}{4}+5\lambda^2=\frac{21\lambda^2}{4}$，所以
$$\frac{21\lambda^2}{4}=21$$
两边同乘 $\frac{4}{21}$ 得 $\lambda^2=4$，即 $\lambda=2$ 或 $\lambda=-2$。

第四步，写出两个切点。$\lambda=2$ 时 $x_0=1$，$y_0=2$，$z_0=2$，切点为 $Q_1(1,2,2)$；$\lambda=-2$ 时 $x_0=-1$，$y_0=-2$，$z_0=-2$，切点为 $Q_2(-1,-2,-2)$。检验两点都在椭球面上：$1^2+2\times 2^2+3\times 2^2=1+8+12=21$；$(-1)^2+2\times(-2)^2+3\times(-2)^2=1+8+12=21$，都成立。

第五步，写切平面方程。在 $Q_1(1,2,2)$ 处法向量为 $\vec{n}_1=(2,8,12)$，约去公因子 $2$ 得 $(1,4,6)$，以它为法向量、过 $Q_1$ 写点法式：
$$1\cdot(x-1)+4\cdot(y-2)+6\cdot(z-2)=0$$
展开：$x-1+4y-8+6z-12=0$，即 $x+4y+6z=21$。

在 $Q_2(-1,-2,-2)$ 处的法向量为 $\vec{n}_2=(-2,-8,-12)$，约去公因子 $-2$ 得 $(1,4,6)$，同样以 $(1,4,6)$ 为法向量、过 $Q_2$ 写点法式：
$$1\cdot(x+1)+4\cdot(y+2)+6\cdot(z+2)=0$$
展开：$x+1+4y+8+6z+12=0$，即 $x+4y+6z=-21$。

第六步，验算。验平行的条件：两个切平面的法向量都是 $(1,4,6)$，与已知平面法向量 $(1,4,6)$ 相同，确实平行，并且它们与已知平面 $x+4y+6z=0$ 都不同（常数项分别是 $21$ 和 $-21$，不是 $0$），符合"平行但不重合"。验切点在切平面上：$1+4\times 2+6\times 2=1+8+12=21$；$-1+4\times(-2)+6\times(-2)=-1-8-12=-21$。两个答案都正确。

**【最终答案】**

$x+4y+6z=21$ 与 $x+4y+6z=-21$

**【易错点】**

第一，容易只写一个答案。$\lambda^2=4$ 给出 $\lambda=\pm 2$ 两组解，对应椭球面两侧的两个切平面，漏掉一个就丢一半分。第二，平行条件必须写成"法向量成比例"并引入参数 $\lambda$，不要直接把 $2x_0=1$、$4y_0=4$、$6z_0=6$ 当成等式硬算，那样只用到比例中的一个特殊情况，会漏解。第三，把切点代回椭球面求 $\lambda$ 时，$\left(\frac{\lambda}{2}\right)^2=\frac{\lambda^2}{4}$，这里的平方容易漏掉。

**【同类题识别技巧】**

以后看到"求曲面上平行于某平面的切平面"或"求曲面上一点使切平面平行于已知平面"，都是同一个套路：设切点，令 $\nabla F$ 与已知法向量成比例，把切点用参数表示，代回曲面方程定参数。若题目改为"切平面垂直于某直线"，则改成 $\nabla F$ 与直线方向向量平行，做法完全一样。

**【一句话总结】**

看到"求平行于某平面的切平面" → 设切点 → $\nabla F$ 与已知法向量成比例（引入参数）→ 代回曲面方程求参数 → 两个解都要写上。

## 8.5 题型五 方向导数与梯度

> **这一类题我到底应该记住什么？**
>
> 这一类题只围绕两个量打转：梯度 $\nabla f=(f_x,f_y)$ 或 $(f_x,f_y,f_z)$，以及方向导数。三条口诀：① 方向导数 = 梯度点乘单位方向向量，也就是 $D_{\vec{l}}f(P)=\nabla f(P)\cdot\frac{\vec{l}}{|\vec{l}|}$，方向向量一定要先单位化，这是最高频的错误点；② 函数值增长最快的方向就是梯度方向 $\nabla f(P)$，此时方向导数取最大值 $|\nabla f(P)|$，减小最快的方向是 $-\nabla f(P)$；③ 梯度垂直于等值线（二元）或等值面（三元），所以"求等值线的切线"时可以拿梯度当法向量。算完以后检查两件事：单位向量的长度是不是 $1$，方向导数的绝对值是不是不超过 $|\nabla f(P)|$。

### 题 8.5-1　【母题】　难度 ★★　建议用时 6分钟　重要程度 ★★★★★

**知识点**：多元微分/方向导数

**【题目】**

求函数 $f(x,y)=x^2+2xy$ 在点 $P(1,2)$ 处沿方向 $\vec{l}=(3,4)$ 的方向导数。（专项训练原创题）

**【考查知识点】**

用"梯度点乘单位方向向量"计算方向导数。

**【题型识别】**

看到题目给了函数、给了点、又给了一个方向向量，问方向导数 → 属于"沿给定方向求方向导数"的题型 → 先求梯度，再把方向向量单位化，最后做点积。

**【需要记住的公式】**

1. 方向导数公式：$D_{\vec{l}}f(P)=\nabla f(P)\cdot\frac{\vec{l}}{|\vec{l}|}=f_x(P)\cos\alpha+f_y(P)\cos\beta$
2. 向量 $(a,b)$ 的单位向量为 $\left(\frac{a}{\sqrt{a^2+b^2}},\frac{b}{\sqrt{a^2+b^2}}\right)$
3. 偏导：$(x^2)_x=2x$，$(2xy)_x=2y$，$(2xy)_y=2x$

**【解题思路】**

方向导数的意思是"沿着某个指定方向走，函数值变化有多快"，所以它只和两件事有关：这一点处函数变化最快方向的快慢程度（梯度），以及指定方向与梯度方向的夹角。把这两件事写成公式就是"梯度点乘单位方向向量"。方向向量 $(3,4)$ 长度是 $5$，不是单位向量，必须先除以 $5$。

**【详细解答】**

第一步，求梯度。对 $x$ 求偏导时把 $y$ 看成常数：$f_x=2x+2y$；对 $y$ 求偏导时把 $x$ 看成常数：$f_y=2x$。在 $P(1,2)$ 处代入：
$$f_x(1,2)=2\times 1+2\times 2=2+4=6,\quad f_y(1,2)=2\times 1=2$$
所以 $\nabla f(P)=(6,2)$。

第二步，把方向向量单位化。方向 $\vec{l}=(3,4)$ 的长度是
$$|\vec{l}|=\sqrt{3^2+4^2}=\sqrt{9+16}=\sqrt{25}=5$$
所以单位方向向量为
$$\vec{e}=\frac{\vec{l}}{|\vec{l}|}=\left(\frac{3}{5},\frac{4}{5}\right)$$

第三步，做点积求方向导数：
$$D_{\vec{l}}f(1,2)=\nabla f(1,2)\cdot\vec{e}=6\times\frac{3}{5}+2\times\frac{4}{5}=\frac{18}{5}+\frac{8}{5}=\frac{26}{5}$$

第四步，用定义验算。沿方向 $\vec{e}$ 从 $P(1,2)$ 出发的参数点为
$$\left(1+\frac{3t}{5},\ 2+\frac{4t}{5}\right)$$
代入函数，记 $g(t)=f\left(1+\frac{3t}{5},2+\frac{4t}{5}\right)$。第一项展开：
$$\left(1+\frac{3t}{5}\right)^2=1+\frac{6t}{5}+\frac{9t^2}{25}$$
第二项先把两个括号相乘再乘 $2$：
$$\left(1+\frac{3t}{5}\right)\left(2+\frac{4t}{5}\right)=2+\frac{4t}{5}+\frac{6t}{5}+\frac{12t^2}{25}$$
再乘 $2$ 得 $4+\frac{8t}{5}+\frac{12t}{5}+\frac{24t^2}{25}$。两项相加，常数部分是 $1+4=5$，恰好等于 $f(1,2)=1^2+2\times 1\times 2=5$；一次项系数是 $\frac{6}{5}+\frac{8}{5}+\frac{12}{5}=\frac{26}{5}$。所以
$$g(t)=5+\frac{26}{5}t+\frac{33t^2}{25}$$
按定义方向导数就是 $g'(0)$，即一次项系数 $\frac{26}{5}$，与第三步结果一致。

**【最终答案】**

$\frac{26}{5}$

**【易错点】**

最大的坑是忘记单位化，直接算 $(6,2)\cdot(3,4)=18+8=26$，这是错的，因为 $(3,4)$ 不是单位向量，长度是 $5$。第二个坑是偏导算错：$f_y=2x$（对 $2xy$ 中的 $y$ 求导，$2x$ 是系数），不要写成 $f_y=2y$。第三，方向导数是一个数，不是向量，答案不要写成坐标形式。

**【同类题识别技巧】**

以后看到"沿方向 $\vec{l}$ 的方向导数"，固定三步：求 $\nabla f(P)$、把 $\vec{l}$ 除以自己的长度、点乘。如果题目给的是"沿 $x$ 轴正向"或"沿 $y$ 轴正向"，单位向量就是 $(1,0)$ 或 $(0,1)$，方向导数退化为偏导数，可以直接用偏导数回答。

**【一句话总结】**

看到沿某方向求方向导数 → 先求梯度，再把方向向量单位化，最后点乘 → 千万别用没单位化的向量。

### 题 8.5-2　【变式】　难度 ★★　建议用时 6分钟　重要程度 ★★★★★

**知识点**：多元微分/梯度

**【题目】**

求函数 $f(x,y,z)=x^2+2y^2+2z^2$ 在点 $P(1,1,1)$ 处函数值增长最快的方向，以及沿这个方向的方向导数（即方向导数的最大值）。（专项训练原创题）

**【考查知识点】**

梯度的几何意义：梯度方向是函数值增长最快的方向，梯度的模是方向导数的最大值。

**【题型识别】**

看到"增长最快""最速上升""上升最陡"或"方向导数的最大值" → 属于梯度的方向与模的题型 → 求出梯度 $\nabla f(P)$，它的方向就是增长最快的方向，它的长度就是最大方向导数。

**【需要记住的公式】**

1. 梯度 $\nabla f(P)=(f_x(P),f_y(P),f_z(P))$
2. 最大方向导数 $=\max\limits_{\vec{e}}D_{\vec{e}}f(P)=|\nabla f(P)|$
3. 向量 $(a,b,c)$ 的单位向量为 $\frac{1}{\sqrt{a^2+b^2+c^2}}(a,b,c)$

**【解题思路】**

所有单位方向的集合是一个长度为 $1$ 的向量，方向导数等于"梯度在这条方向上的投影"，投影最大发生在方向与梯度同向的时候，此时投影长度正好是梯度自身的长度。所以本题只要算两样东西：梯度本身（给出方向），梯度的模（给出最大值）。

**【详细解答】**

第一步，求三个偏导数。对 $x$ 求偏导时把 $y,z$ 看成常数：$f_x=2x$；对 $y$ 求偏导时把 $x,z$ 看成常数：$f_y=4y$；对 $z$ 求偏导时把 $x,y$ 看成常数：$f_z=4z$。

第二步，代点求梯度。在 $P(1,1,1)$ 处代入三个偏导：
$$f_x(P)=2\times 1=2,\quad f_y(P)=4\times 1=4,\quad f_z(P)=4\times 1=4$$
所以
$$\nabla f(P)=(2,4,4)$$

第三步，写出增长最快的方向。增长最快的方向就是梯度方向，把梯度化成单位向量作为最终的"方向"：
$$|\nabla f(P)|=\sqrt{2^2+4^2+4^2}=\sqrt{4+16+16}=\sqrt{36}=6$$
所以增长最快的方向为
$$\frac{\nabla f(P)}{|\nabla f(P)|}=\left(\frac{2}{6},\frac{4}{6},\frac{4}{6}\right)=\left(\frac{1}{3},\frac{2}{3},\frac{2}{3}\right)$$
（若只要求方向，直接回答"梯度方向 $(2,4,4)$，即从 $P$ 点沿 $(2,4,4)$ 出发的方向"也是正确的。）

第四步，写出方向导数的最大值。沿梯度方向的方向导数取最大，最大值等于梯度的模：
$$\max D_{\vec{e}}f(P)=|\nabla f(P)|=6$$

第五步，验算。先验单位向量：$\left(\frac{1}{3}\right)^2+\left(\frac{2}{3}\right)^2+\left(\frac{2}{3}\right)^2=\frac{1}{9}+\frac{4}{9}+\frac{4}{9}=1$，长度确实是 $1$。再验最大性：沿这个方向做点积，$\nabla f(P)\cdot\left(\frac{1}{3},\frac{2}{3},\frac{2}{3}\right)=\frac{2}{3}+\frac{8}{3}+\frac{8}{3}=\frac{18}{3}=6$，等于梯度的模；换一个方向试，比如沿 $(1,0,0)$，方向导数是 $2$，比 $6$ 小，符合"梯度方向最大"的结论。另外，沿 $-\nabla f(P)$ 方向的方向导数是 $-6$，那是函数值下降最快的方向。

**【最终答案】**

增长最快的方向为 $\left(\frac{1}{3},\frac{2}{3},\frac{2}{3}\right)$（即梯度方向 $(2,4,4)$），最大方向导数为 $6$

**【易错点】**

第一，把"方向"写成 $(2,4,4)$ 有时会被判为没有单位化：如果题目问"方向"并要求写成方向余弦，必须除以模 $6$，写成 $\left(\frac{1}{3},\frac{2}{3},\frac{2}{3}\right)$；如果题目只问"沿哪个方向"，$(2,4,4)$ 也可以接受，但回答时说明它是梯度方向最稳妥。第二，最大值是梯度的模 $6$，不是梯度本身，答案不能只写 $(2,4,4)$。第三，$f_z=4z$ 在 $z=1$ 处是 $4$，不要因为 $z$ 的系数是 $2$ 就把偏导写成 $2$。

**【同类题识别技巧】**

以后看到"增长最快 / 最速上升 / 上升最陡 / 方向导数最大值 / 方向导数最小"，全都先求梯度：最快上升方向是 $\nabla f(P)$，最大值是 $|\nabla f(P)|$；最快下降方向是 $-\nabla f(P)$，最小值是 $-|\nabla f(P)|$。

**【一句话总结】**

看到"增长最快的方向" → 求梯度 → 方向就是 $\nabla f(P)$（要方向余弦就除以模），最大方向导数就是 $|\nabla f(P)|$。

### 题 8.5-3　【变式】　难度 ★★　建议用时 7分钟　重要程度 ★★★★

**知识点**：多元微分/梯度

**【题目】**

已知曲线 $C$ 由方程 $x^2+xy+y^2=3$ 给出，利用"梯度垂直于等值线"这一性质，求 $C$ 在点 $P(1,1)$ 处的切线方程。（根据 CMC 常见题型改编）

**【考查知识点】**

等值线的法向量是梯度，由此把"求等值线切线"化为"用法向量写直线"。

**【题型识别】**

看到二元方程 $f(x,y)=c$ 表示一条曲线（等值线），问这条曲线在某点的切线 → 属于"梯度与等值线垂直"的题型 → 令 $F(x,y)=f(x,y)-c$，求出 $\nabla F(P)$，它垂直于曲线，所以把它当作切线的法向量写直线方程。

**【需要记住的公式】**

1. 等值线 $F(x,y)=c$ 上点 $P$ 处的法向量为 $\nabla F(P)=(F_x(P),F_y(P))$
2. 梯度与等值线在该点的切线互相垂直
3. 以 $(A,B)$ 为法向量、过 $(x_0,y_0)$ 的直线：$A(x-x_0)+B(y-y_0)=0$

**【解题思路】**

一元函数的图像是曲线，二元函数的等值线也是曲线。梯度指向函数值增长最快的方向，它必然"横穿"等值线，因此垂直于等值线。于是一个本来要用隐函数求导解决的切线问题，可以换成"求梯度当法向量"的直线问题，计算量小很多。

**【详细解答】**

第一步，写成等值线形式并检验点。令
$$F(x,y)=x^2+xy+y^2-3$$
曲线 $C$ 就是 $F(x,y)=0$。把 $P(1,1)$ 代入：
$$F(1,1)=1^2+1\times 1+1^2-3=1+1+1-3=0$$
所以 $P$ 在曲线 $C$ 上。

第二步，求梯度。对 $x$ 求偏导时把 $y$ 看成常数：$F_x=2x+y$；对 $y$ 求偏导时把 $x$ 看成常数：$F_y=x+2y$。在 $P(1,1)$ 处代入：
$$F_x(1,1)=2\times 1+1=3,\quad F_y(1,1)=1+2\times 1=3$$
所以
$$\nabla F(P)=(3,3)$$

第三步，把它当作切线的法向量写切线。梯度垂直于等值线的切线，所以切线以 $(3,3)$ 为法向量，过点 $P(1,1)$：
$$3(x-1)+3(y-1)=0$$
两边同除以 $3$：$(x-1)+(y-1)=0$，即
$$x+y=2$$

第四步，用隐函数求导验算。对 $x^2+xy+y^2=3$ 两边求全微分，注意 $xy$ 要用乘积法则：
$$(2x+y)\,dx+(x+2y)\,dy=0$$
在 $P(1,1)$ 处 $2x+y=3$、$x+2y=3$，所以
$$3\,dx+3\,dy=0$$
即 $\frac{dy}{dx}=-1$，切线斜率是 $-1$。过 $P(1,1)$ 的切线是 $y-1=-(x-1)$，写成 $x+y=2$，与第三步一致。再验两个向量的垂直关系：切线的方向向量可取 $(1,-1)$，它与梯度 $(3,3)$ 的点积是 $1\times 3+(-1)\times 3=0$，确实垂直。

**【最终答案】**

$x+y=2$

**【易错点】**

第一，梯度的两个分量 $F_x=2x+y$、$F_y=x+2y$ 容易写混，交叉项 $xy$ 对 $x$ 求导得 $y$、对 $y$ 求导得 $x$，不能都写成 $2x$ 或 $2y$。第二，梯度是切线的法向量，不是方向向量；如果误把 $(3,3)$ 当方向向量，会得到 $x-y=0$ 这个错误答案，用"斜率 $-1$"验算立刻能发现。第三，写直线前要确认点确实在曲线上。

**【同类题识别技巧】**

以后看到"由方程 $f(x,y)=c$ 给出的曲线，求某点切线或法线"，直接求梯度：切线以 $\nabla f$ 为法向量，法线以 $\nabla f$ 为方向向量。三元情形完全一样，等值面 $F(x,y,z)=c$ 的切平面就以 $\nabla F$ 为法向量（这正是 8.4 节的做法）。

**【一句话总结】**

看到等值线 $f(x,y)=c$ 求切线 → 求梯度 $\nabla f(P)$ → 梯度是法向量，切线就写 $f_x(P)(x-x_0)+f_y(P)(y-y_0)=0$。

### 题 8.5-4　【变式】　难度 ★★　建议用时 7分钟　重要程度 ★★★★

**知识点**：多元微分/方向导数

**【题目】**

求函数 $f(x,y,z)=x^2yz$ 在点 $P(1,1,1)$ 处沿方向 $\vec{l}=(1,2,-2)$ 的方向导数。（专项训练原创题）

**【考查知识点】**

三元函数的方向导数：梯度与单位方向向量的点积。

**【题型识别】**

看到三元函数、给定点、给定方向向量，问方向导数 → 属于"沿给定方向求方向导数"的题型 → 求三个偏导组成梯度，把方向向量单位化，再做点积。三元比二元只多一个分量，步骤完全一样。

**【需要记住的公式】**

1. $D_{\vec{l}}f(P)=\nabla f(P)\cdot\frac{\vec{l}}{|\vec{l}|}=f_x(P)\cos\alpha+f_y(P)\cos\beta+f_z(P)\cos\gamma$
2. 向量 $(a,b,c)$ 的单位向量为 $\frac{1}{\sqrt{a^2+b^2+c^2}}(a,b,c)$
3. 偏导（把另外两个变量看成常数）：$(x^2yz)_x=2xyz$，$(x^2yz)_y=x^2z$，$(x^2yz)_z=x^2y$

**【解题思路】**

思路和二元情形一字不差：先求梯度，再单位化方向向量，最后点乘。这里的偏导数都是乘积形式，逐个变量求导时把其余变量当常数即可。方向向量 $(1,2,-2)$ 的长度是 $3$。

**【详细解答】**

第一步，求三个偏导数。求 $f_x$ 时把 $y,z$ 看成常数：$f_x=2xyz$；求 $f_y$ 时把 $x,z$ 看成常数：$f_y=x^2z$；求 $f_z$ 时把 $x,y$ 看成常数：$f_z=x^2y$。

第二步，代点求梯度。在 $P(1,1,1)$ 处代入：
$$f_x(P)=2\times 1\times 1\times 1=2,\quad f_y(P)=1^2\times 1=1,\quad f_z(P)=1^2\times 1=1$$
所以 $\nabla f(P)=(2,1,1)$。

第三步，把方向向量单位化。方向 $\vec{l}=(1,2,-2)$ 的长度是
$$|\vec{l}|=\sqrt{1^2+2^2+(-2)^2}=\sqrt{1+4+4}=\sqrt{9}=3$$
所以单位方向向量为
$$\vec{e}=\left(\frac{1}{3},\frac{2}{3},-\frac{2}{3}\right)$$

第四步，做点积求方向导数：
$$D_{\vec{l}}f(1,1,1)=\nabla f(1,1,1)\cdot\vec{e}=2\times\frac{1}{3}+1\times\frac{2}{3}+1\times\left(-\frac{2}{3}\right)=\frac{2+2-2}{3}=\frac{2}{3}$$

第五步，用定义验算。沿单位方向 $\vec{e}$ 从 $P$ 出发的参数点是
$$\left(1+\frac{t}{3},\ 1+\frac{2t}{3},\ 1-\frac{2t}{3}\right)$$
代入函数，记 $g(t)=f\left(1+\frac{t}{3},1+\frac{2t}{3},1-\frac{2t}{3}\right)$。先算后两个括号的乘积：
$$\left(1+\frac{2t}{3}\right)\left(1-\frac{2t}{3}\right)=1-\frac{4t^2}{9}$$
再乘第一个括号的平方：
$$g(t)=\left(1+\frac{t}{3}\right)^2\left(1-\frac{4t^2}{9}\right)=\left(1+\frac{2t}{3}+\frac{t^2}{9}\right)\left(1-\frac{4t^2}{9}\right)$$
展开后，常数项是 $1$（等于 $f(1,1,1)=1$），一次项只来自 $1\times\frac{2t}{3}$，即系数为 $\frac{2}{3}$。按定义方向导数等于 $g'(0)=\frac{2}{3}$，与第四步一致。

**【最终答案】**

$\frac{2}{3}$

**【易错点】**

第一，方向向量长度算错：$\sqrt{1+4+4}=3$，别把 $(-2)^2$ 当成 $-4$ 而得到 $\sqrt{1}$。第二，三元函数的偏导要注意"对谁求导，其余全是常数"：$f_y=x^2z$ 中 $z$ 是常数因子，不能写成 $x^2yz$。第三，单位向量第三个分量是负的 $-\frac{2}{3}$，点积时符号不要丢，否则会算成 $\frac{2+2+2}{3}=2$。

**【同类题识别技巧】**

以后遇到三元函数的方向导数，步骤与二元完全一致，只是梯度多一个分量、单位化时多开一个平方项。最后可以用 $|D_{\vec{l}}f(P)|\leq|\nabla f(P)|$ 检查：本题 $|\nabla f(P)|=\sqrt{4+1+1}=\sqrt{6}\approx 2.45$，而 $\frac{2}{3}\approx 0.67$ 不超过它，结果合理。

**【一句话总结】**

看到三元函数沿给定方向求方向导数 → 求三个偏导得梯度 → 方向向量除以自己的长度 → 点乘得一个数。

### 题 8.5-5　【基础训练】　难度 ★　建议用时 4分钟　重要程度 ★★★★

**知识点**：多元微分/梯度

**【题目】**

求函数 $f(x,y)=x^2+3xy$ 在点 $P(1,2)$ 处的梯度。（专项训练原创题）

**【考查知识点】**

梯度的定义与二元函数偏导数的计算。

**【题型识别】**

看到题目直接问"求梯度" → 属于梯度计算的基础题型 → 分别求出两个偏导数，代点后写成向量 $(f_x(P),f_y(P))$ 即可，不需要单位化，也不需要求方向导数。

**【需要记住的公式】**

1. 梯度 $\nabla f(P)=(f_x(P),f_y(P))$
2. 偏导：$(x^2)_x=2x$，$(3xy)_x=3y$，$(3xy)_y=3x$

**【解题思路】**

梯度就是把两个偏导数按顺序摆成一个向量。求 $f_x$ 时把 $y$ 看成常数，求 $f_y$ 时把 $x$ 看成常数。这一题是纯计算题，用来熟悉"梯度是一个向量"这件事。

**【详细解答】**

第一步，求对 $x$ 的偏导数。把 $y$ 看成常数，$x^2$ 的导数是 $2x$，$3xy$ 中 $3y$ 是系数，对 $x$ 求导得 $3y$，所以
$$f_x=2x+3y$$

第二步，求对 $y$ 的偏导数。把 $x$ 看成常数，$x^2$ 与 $y$ 无关，导数为 $0$，$3xy$ 中 $3x$ 是系数，对 $y$ 求导得 $3x$，所以
$$f_y=3x$$

第三步，代点。在 $P(1,2)$ 处：
$$f_x(1,2)=2\times 1+3\times 2=2+6=8,\quad f_y(1,2)=3\times 1=3$$
所以梯度为
$$\nabla f(1,2)=(8,3)$$

第四步，验算。用"偏导数就是沿坐标轴方向的方向导数"来检查：沿 $x$ 轴正向移动一小步，函数值的变化率应为 $8$；沿 $y$ 轴正向移动一小步，变化率应为 $3$。另外梯度向量的模是
$$|\nabla f(1,2)|=\sqrt{8^2+3^2}=\sqrt{64+9}=\sqrt{73}$$
这说明在 $P$ 点沿梯度方向的方向导数是 $\sqrt{73}$，它应当大于等于沿 $x$、$y$ 轴方向的方向导数 $8$ 和 $3$，因为 $\sqrt{73}\approx 8.54>8>3$，符合"梯度方向增长最快"的结论。

**【最终答案】**

$\nabla f(1,2)=(8,3)$

**【易错点】**

第一，$f_y=3x$，不要写成 $3y$ 或 $3xy$：对 $y$ 求导时 $3x$ 是常数系数。第二，$x^2$ 对 $y$ 求导是 $0$，不能保留下来。第三，梯度是向量，答案要写成 $(8,3)$ 这样的坐标形式，写成单独一个数 $8$ 就漏了一半信息。第四，这题不需要单位化，别多做一步。

**【同类题识别技巧】**

以后凡是题目说"求梯度"，就把各偏导数代点后排成向量；如果紧接着又问"沿某方向的方向导数"或"增长最快的方向"，再在梯度基础上单位化或求模。梯度是这一类题的"通用零件"，先算准它，后面的问题都好办。

**【一句话总结】**

看到"求梯度" → 逐个变量求偏导（其余变量当常数）→ 代点 → 排成向量 $(f_x,f_y)$，不要单位化。
