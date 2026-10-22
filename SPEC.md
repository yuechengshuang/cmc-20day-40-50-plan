# 内容文件写作规范（必须严格遵守）

你在为「CMC（中国大学生数学竞赛）非数学类初赛、当前约 20 分、基础薄弱」的学生写教辅。
铁律：**基础题 > 常规题 > 中档题 > 难题**。禁止炫技，禁止偏题怪题，禁止跳步。
所有解析必须让「公式都记不清」的学生能一步步看懂并自己算出来。

## 一、文件格式（UTF-8 纯文本，扩展名 .txt）

标记行必须**独占一行**，以 `@@` 开头。除 `@@PROBLEM` 行外，标记行内不得有其他内容。

```
@@CHAPTER 第四章 极限与连续（专项题库）

@@GUIDE
本章拿分指南正文，可以分多段。
可以用 - 开头的列表行。
@@GUIDEEND

@@SECTION 4.1 题型一 等价无穷小替换

@@METHOD
这一类题我到底应该记住什么？用 3~5 句话总结该题型。
@@METHODEND

@@PROBLEM id=4.1-1 type=母题 star=★★ time=6分钟 imp=★★★★★ kp=极限/等价无穷小替换
@@STEM
题干写在这里，公式用 $...$。多段之间空一行。
@@POINT
考查知识点（一句话）
@@IDENTIFY
题型识别：看到……特征 → 属于……题型 → 用……方法。
@@FORMULAS
1. 公式一（用 $...$ 写）
2. 公式二
@@IDEA
解题思路：先用通俗语言讲清楚为什么这么做。
@@SOLUTION
详细解答。关键代数变形、求导、积分步骤一步一步写。
分段时中间空一行。
@@ANSWER
最终答案（用 $...$ 写）
@@PITFALL
易错点：学生最可能错在哪里。
@@TIPS
同类题识别技巧：以后看到什么特征继续用这个方法。
@@SUMMARY
一句话总结（给条件反射口令）。
@@ENDPROBLEM

@@PROBLEM id=4.1-2 type=变式 star=★★ time=6分钟 imp=★★★★★ kp=极限/等价无穷小替换
……（同样的字段顺序，字段名不可缺、不可改名、不可换顺序）
@@ENDPROBLEM
```

### @@PROBLEM 行属性规则
- `id=`：形如 `4.1-1`。即「章节号.题型号-题目序号」。同文件内唯一、递增。
- `type=`：`母题` / `变式` / `基础训练` / `提高训练` 四者之一。
- `star=`：`★` / `★★` / `★★★` / `★★★★` 之一（以 ★、★★、★★★ 为主）。
- `time=`：如 `5分钟`、`8分钟`、`12分钟`。
- `imp=`：`★★★★★` / `★★★★` / `★★★` 之一。
- `kp=`：知识点路径，如 `极限/洛必达法则`、`积分/分部积分`。

### 题目组织规则
- 每个 `@@SECTION` 下：**第 1 题必须是 `type=母题`**，紧接着 2~4 题 `type=变式`（母题讲透，变式改参数/改形式/改条件/改问法/改计算方式），之后可以放 `基础训练`、`提高训练`。
- 每个 `@@SECTION` 结束前（最后一个 `@@ENDPROBLEM` 之后、下一个 `@@SECTION` 之前）**必须**有 `@@METHOD ... @@METHODEND`，放在 SECTION 的第一个位置（紧跟 @@SECTION 行之后）。

## 二、公式规范（极重要）

- 行内公式：`$ ... $`
- 独立成行公式：整行只写 `$$ ... $$`
- `$` 必须配对；正文里不要出现孤立的 `$`。
- 中文不能出现在 `$...$` 里，除非包在 `\text{...}` 内。也不要在 `$...$` 里写字数说明。

### 允许使用的 LaTeX 命令（白名单，其他一律不许出现）
`\frac \dfrac \tfrac \sqrt \overline \underline \bar \vec \hat \tilde \dot \ddot`
`^ _ ' \left \right \big \Big \bigg \Bigg`
`\int \iint \iiint \oint \sum \prod \lim \limsup \liminf \max \min \sup \inf`
`\to \rightarrow \leftarrow \Rightarrow \Leftarrow \Leftrightarrow \infty`
`\cdot \times \div \pm \mp \circ \ast`
`\leq \geq \neq \approx \equiv \sim \cong \propto`
`\in \notin \subset \subseteq \cup \cap \setminus \emptyset \forall \exists`
`\partial \nabla`
希腊字母：`\alpha \beta \gamma \delta \epsilon \varepsilon \zeta \eta \theta \lambda \mu \nu \xi \pi \rho \sigma \tau \varphi \phi \chi \psi \omega \Delta \Gamma \Theta \Lambda \Sigma \Omega`
函数名：`\sin \cos \tan \cot \sec \csc \arcsin \arccos \arctan \sinh \cosh \tanh \ln \lg \log \exp \det \gcd \deg`
其他：`\cdots \ldots \dots \vdots \ddots \quad \qquad \, \; \: \text{} \mathrm{} \mathbb{R} \mathbb{N} \mathbb{Z} \mathbb{C} \mathbb{Q}`
`\begin{cases} ... \end{cases}`（列用 `&` 分隔，行用 `\\` 分隔）
转义字符：`\{ \} \% \_ \& \#`

### 明令禁止
`\begin{align}`、`\begin{matrix}` 等一切 align/gather/matrix 环境、`\stackrel`、`\overset`、`\underset`、`\substack`、`\displaystyle`、`\limits`、`\binom`、`\tag`、`\hspace`、`\phantom`、`\mathbf`、`\displaystyle`、自定义宏。

公式写法示例：
- `$\lim_{x\to 0}\frac{\sin x}{x}=1$`
- `$\int_0^1 x^2\,dx=\frac13$`
- `$$f'(x)=2x+\frac{1}{x}\quad(x>0)$$`
- `$f(x)=\begin{cases} x^2, & x\geq 0 \\ -x, & x<0 \end{cases}$`（注意行内 cases 也写作一行）
- `$\text{原式}=\lim_{x\to 0}\frac{1-\cos x}{x^2}$`

## 三、文字要求

- **严禁**出现：「显然」「易知」「由常规方法可得」「计算即得」「略」「不难看出」「同理（除非结构完全一样且已写清）」「整理得（后面直接蹦答案）」。
- 【详细解答】必须写出关键中间步骤：换元写清换成了什么、分部积分写清 $u$ 和 $dv$ 的取法、求导写清用了哪条求导法则、代入上下限写清代入过程。如果实际要算 3~4 步，就写 3~4 步。
- 每道题写完后，**自己重新验算一遍答案**（极限值、导数值、积分值、通解、收敛性都要验算）。答案错了比不写还糟。
- 【需要记住的公式】列 1~4 条本题真正用到的基础公式。
- 【一句话总结】必须是「看到 X → 想 Y」这种条件反射口令。
- 【易错点】要说具体，例如「忘记 $\ln$ 中真数必须大于 0，导致漏掉定义域」。

## 四、自检（交稿前必做）

写完后运行（把 `<文件>` 换成你的文件）：
```
& "C:\Users\联想\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe" "C:\Users\联想\Desktop\AI学习工作台\CMC_20天冲刺\build\check_content.py" "C:\Users\联想\Desktop\AI学习工作台\CMC_20天冲刺\content\<文件>"
```
必须看到 **格式检查通过**、**公式解析：0 处失败**、**禁止用语：0 处**。
若有任何错误，逐一修好，再重新运行，直到完全通过为止。

## 五、模拟卷文件格式（只用于写模拟卷时）

模拟卷**不用** `@@CHAPTER` / `@@SECTION` / `@@METHOD`，改用：

```
@@MOCK 模拟卷（一）

@@INFO
（这里写：试卷结构说明、时间分配、难度分析、分层目标——哪些题是20分水平该做出来的、
  哪些是40分水平该做出来的、哪些是50分目标争取题、以及建议得分目标。可以分多段、用 - 列表）
@@INFOEND

@@PROBLEM id=M1-1 score=6 type=填空 star=★★ time=5分钟 imp=★★★★★ kp=极限/等价无穷小
@@STEM
题干。题干末尾用括号注明来源，例如（根据 CMC 常见题型改编）。
@@POINT
……
（以下字段与普通题完全一致，共 10 个字段，最后 @@ENDPROBLEM）
@@ENDPROBLEM
```

- `type=` 只能是 `填空`（每题 6 分）或 `解答`（每题 14 分）。
- 必须写 `score=`，填空题 `score=6`，解答题 `score=14`。
- 一道题一个 `@@PROBLEM`，字段顺序、字段名与普通题完全相同。
- 同一套模拟卷如果拆成两个文件写，两个文件的 `@@MOCK` 标题必须**完全一致**。