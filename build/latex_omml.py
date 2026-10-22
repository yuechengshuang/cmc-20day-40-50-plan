# -*- coding: utf-8 -*-
"""LaTeX(白名单子集) -> OMML 转换器：让 python-docx 输出 Word 原生公式。

用法：
    from latex_omml import omml_element, omml_xml, LatexError
    el = omml_element(r"\\lim_{x\\to 0}\\frac{\\sin x}{x}")   # 行内
    el = omml_element(r"\\int_0^1 x\\,dx", display=True)      # 独立公式行
    p._p.append(el)
"""
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

NSDECL = nsdecls('m', 'w')

GREEK = {
    'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'delta': 'δ', 'epsilon': 'ε',
    'varepsilon': 'ε', 'zeta': 'ζ', 'eta': 'η', 'theta': 'θ', 'vartheta': 'ϑ',
    'iota': 'ι', 'kappa': 'κ', 'lambda': 'λ', 'mu': 'μ', 'nu': 'ν', 'xi': 'ξ',
    'pi': 'π', 'rho': 'ρ', 'sigma': 'σ', 'tau': 'τ', 'upsilon': 'υ',
    'phi': 'φ', 'varphi': 'φ', 'chi': 'χ', 'psi': 'ψ', 'omega': 'ω',
    'Gamma': 'Γ', 'Delta': 'Δ', 'Theta': 'Θ', 'Lambda': 'Λ', 'Xi': 'Ξ',
    'Pi': 'Π', 'Sigma': 'Σ', 'Upsilon': 'Υ', 'Phi': 'Φ', 'Psi': 'Ψ', 'Omega': 'Ω',
}

SYM = {
    'infty': '∞', 'to': '→', 'rightarrow': '→', 'Rightarrow': '⇒',
    'leftarrow': '←', 'Leftarrow': '⇐', 'leftrightarrow': '↔',
    'Leftrightarrow': '⇔', 'mapsto': '↦', 'cdot': '·', 'times': '×',
    'div': '÷', 'pm': '±', 'mp': '∓', 'ast': '∗', 'star': '⋆', 'circ': '∘',
    'bullet': '•', 'oplus': '⊕', 'otimes': '⊗', 'leq': '≤', 'le': '≤',
    'geq': '≥', 'ge': '≥', 'neq': '≠', 'ne': '≠', 'approx': '≈',
    'equiv': '≡', 'sim': '∼', 'cong': '≅', 'propto': '∝', 'll': '≪',
    'gg': '≫', 'in': '∈', 'notin': '∉', 'subset': '⊂', 'subseteq': '⊆',
    'supset': '⊃', 'supseteq': '⊇', 'cup': '∪', 'cap': '∩',
    'setminus': '\\', 'emptyset': '∅', 'varnothing': '∅', 'forall': '∀',
    'exists': '∃', 'neg': '¬', 'land': '∧', 'lor': '∨', 'partial': '∂',
    'nabla': '∇', 'cdots': '⋯', 'ldots': '…', 'dots': '…', 'vdots': '⋮',
    'ddots': '⋱', 'prime': '′', 'angle': '∠', 'because': '∵',
    'therefore': '∴', 'degree': '°', 'lvert': '|', 'rvert': '|',
    'lVert': '‖', 'rVert': '‖', 'mid': '|', 'langle': '⟨', 'rangle': '⟩',
    'ell': 'ℓ', 'hbar': 'ℏ', 'Longrightarrow': '⟹', 'Longleftrightarrow': '⟺',
    'iff': '⇔', 'implies': '⇒', 'impliedby': '⇐', 'geqslant': '≥',
    'leqslant': '≤', 'lfloor': '⌊', 'rfloor': '⌋', 'lceil': '⌈',
    'rceil': '⌉', 'colon': ':', 'simeq': '≃', 'approxeq': '≊',
    'varsigma': 'ς', 'digamma': 'ϝ', 'aleph': 'ℵ', 'Re': 'Re', 'Im': 'Im',
    'triangleq': '≜', 'lesssim': '≲', 'gtrsim': '≳', 'nmid': '∤',
    'bigcup': '⋃', 'bigcap': '⋂', 'bigoplus': '⨁', 'bigotimes': '⨂',
}

FUNCS = ['arcsin', 'arccos', 'arctan', 'arccot', 'arcsec', 'arccsc',
         'sinh', 'cosh', 'tanh', 'sech', 'csch', 'sin', 'cos',
         'tan', 'cot', 'sec', 'csc', 'ln', 'lg', 'log', 'exp', 'det', 'dim',
         'gcd', 'deg', 'arg', 'sgn']

LIMITS = ['lim', 'limsup', 'liminf', 'max', 'min', 'sup', 'inf']
LIMIT_TEXT = {'limsup': 'lim sup', 'liminf': 'lim inf'}

NARY = {'sum': '∑', 'prod': '∏', 'int': '∫', 'iint': '∬', 'iiint': '∭',
        'oint': '∮'}

SPACES = {'\\,': '\u2009', '\\:': '\u2005', '\\;': '\u2004', '\\!': '',
          '\\ ': '\u2009', '\\quad': '\u2003', '\\qquad': '\u2003\u2003'}

SIZE_HINTS = {'big', 'Big', 'bigg', 'Bigg', 'bigl', 'bigr', 'Bigl', 'Bigr',
              'biggl', 'biggr', 'Biggl', 'Biggr', 'bigm', 'Bigm', 'middle',
              'limits', 'nolimits', 'displaystyle', 'textstyle',
              'scriptstyle', 'not'}

ACCENT = {'vec': '⃗', 'hat': '^', 'widehat': '^', 'tilde': '~',
          'widetilde': '~', 'dot': '˙', 'ddot': '¨', 'bar': '¯',
          'overline': '¯', 'check': 'ˇ', 'breve': '˘'}

MATHBB = {'R': 'ℝ', 'N': 'ℕ', 'Z': 'ℤ', 'C': 'ℂ', 'Q': 'ℚ', 'P': 'ℙ'}


class LatexError(Exception):
    pass


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def _is_cjk(t):
    for ch in t:
        if '\u3000' <= ch <= '\u9fff' or '\uff00' <= ch <= '\uffef':
            return True
    return False


def run_xml(text, sty=None):
    """sty: None=默认(斜体变量) 'p'=正体 'b'=粗体"""
    if not text:
        return ''
    rpr = ''
    if sty == 'p':
        rpr = '<m:rPr><m:sty m:val="p"/></m:rPr>'
    elif sty == 'b':
        rpr = '<m:rPr><m:sty m:val="b"/></m:rPr>'
    ea = ''
    if _is_cjk(text):
        ea = ' w:eastAsia="宋体"'
    return ('<m:r>' + rpr +
            '<w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"'
            + ea + '/></w:rPr>' +
            '<m:t xml:space="preserve">' + esc(text) + '</m:t></m:r>')


class Parser(object):
    def __init__(self, s, display=False):
        self.s = s
        self.i = 0
        self.display = display

    # ---------- 基础工具 ----------
    def eof(self):
        return self.i >= len(self.s)

    def skip_ws(self):
        while self.i < len(self.s) and self.s[self.i] in ' \t\n\r':
            self.i += 1

    def at_cmd(self, name):
        if not self.s.startswith('\\' + name, self.i):
            return False
        k = self.i + 1 + len(name)
        return k >= len(self.s) or not self.s[k].isalpha()

    def _raw_group(self):
        """读取一个 {..} 的原始内容（不解析），用于 \\text / \\begin 等。"""
        self.skip_ws()
        if self.eof() or self.s[self.i] != '{':
            raise LatexError('期望 {')
        depth = 0
        j = self.i
        while j < len(self.s):
            if self.s[j] == '\\':
                j += 2
                continue
            if self.s[j] == '{':
                depth += 1
            elif self.s[j] == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= len(self.s):
            raise LatexError('缺少 }')
        content = self.s[self.i + 1:j]
        self.i = j + 1
        return content

    @staticmethod
    def _unescape_text(t):
        out = []
        k = 0
        while k < len(t):
            if t[k] == '\\' and k + 1 < len(t) and t[k + 1] in '%_&$#{}':
                out.append(t[k + 1])
                k += 2
            else:
                out.append(t[k])
                k += 1
        return ''.join(out)

    def parse_arg(self):
        """解析一个参数：{...} 或单个 token（LaTeX 语义：\\frac13 = \\frac{1}{3}）。"""
        self.skip_ws()
        if self.eof():
            raise LatexError('参数缺失')
        if self.s[self.i] == '{':
            self.i += 1
            inner = self.parse_seq(stop='}')
            if self.i < len(self.s) and self.s[self.i] == '}':
                self.i += 1
            else:
                raise LatexError('缺少 }')
            return inner
        if self.s[self.i] == '\\':
            xml, kind = self.parse_command()
            if kind == 'nary':
                return self.build_nary(xml, None, None, '')
            return xml
        c = self.s[self.i]
        self.i += 1
        return run_xml(c)

    # ---------- 主解析 ----------
    def parse_all(self):
        out = self.parse_seq()
        self.skip_ws()
        if not self.eof():
            raise LatexError('多余的 } 或未识别内容: ' + self.s[self.i:self.i + 12])
        return out

    def parse_seq(self, stop=''):
        out = []
        while not self.eof():
            c = self.s[self.i]
            if c == '}':
                break
            if stop and c in stop:
                break
            if c == '&' or (c == '\\' and self.s.startswith('\\\\', self.i)):
                break
            if self.at_cmd('right') or self.at_cmd('end'):
                break
            out.append(self.parse_scripted(stop))
        return ''.join(out)

    def parse_scripted(self, stop=''):
        base, kind = self.parse_atom()
        sub = sup = None
        while not self.eof():
            c = self.s[self.i]
            if c == '^' or c == '_':
                self.i += 1
                arg = self.parse_arg()
                if c == '^':
                    sup = (sup or '') + arg
                else:
                    sub = (sub or '') + arg
            elif c == "'":
                self.i += 1
                sup = (sup or '') + run_xml('′', 'p')
            else:
                break
        if kind == 'nary':
            return self.build_nary(base, sub, sup, stop)
        if sub and sup:
            return ('<m:sSubSup><m:e>' + base + '</m:e><m:sub>' + sub +
                    '</m:sub><m:sup>' + sup + '</m:sup></m:sSubSup>')
        if sub:
            if kind == 'lim':
                return ('<m:limLow><m:e>' + base + '</m:e><m:lim>' + sub +
                        '</m:lim></m:limLow>')
            return ('<m:sSub><m:e>' + base + '</m:e><m:sub>' + sub +
                    '</m:sub></m:sSub>')
        if sup:
            return ('<m:sSup><m:e>' + base + '</m:e><m:sup>' + sup +
                    '</m:sup></m:sSup>')
        return base

    def build_nary(self, chrval, sub, sup, stop):
        body = self.parse_seq(stop=stop + '+-=,;>')
        limloc = 'undOvr' if (self.display and chrval in ('∑', '∏')) else 'subSup'
        return ('<m:nary><m:naryPr><m:chr m:val="' + esc(chrval) +
                '"/><m:limLoc m:val="' + limloc + '"/>' +
                '<m:subHide m:val="%d"/><m:supHide m:val="%d"/></m:naryPr>'
                % (0 if sub else 1, 0 if sup else 1) +
                '<m:sub>' + (sub or '') + '</m:sub>' +
                '<m:sup>' + (sup or '') + '</m:sup>' +
                '<m:e>' + body + '</m:e></m:nary>')

    def parse_atom(self):
        s = self.s
        if self.eof():
            raise LatexError('内容意外结束')
        c = s[self.i]
        if c == '{':
            self.i += 1
            inner = self.parse_seq(stop='}')
            if self.i < len(s) and s[self.i] == '}':
                self.i += 1
            else:
                raise LatexError('缺少 }')
            return inner, 'char'
        if c == '\\':
            return self.parse_command()
        if c in ' \t\n\r':
            self.skip_ws()
            return '', 'char'
        # 普通字符：连续字母数字(. 也算)合成一个 run
        if c.isalnum() or c in '.':
            j = self.i
            while j < len(s) and (s[j].isalnum() or s[j] == '.'):
                j += 1
            text = s[self.i:j]
            self.i = j
            return run_xml(text), 'char'
        # 其他单字符（括号、运算符、逗号等）
        self.i += 1
        return run_xml(c), 'char'

    def _delim(self):
        self.skip_ws()
        if self.eof():
            return ''
        c = self.s[self.i]
        if c == '.':
            self.i += 1
            return ''
        if c == '\\':
            j = self.i + 1
            if j < len(self.s) and not self.s[j].isalpha():
                ch = self.s[j]
                self.i = j + 1
                return {'{': '{', '}': '}', '|': '‖'}.get(ch, ch)
            k = j
            while k < len(self.s) and self.s[k].isalpha():
                k += 1
            name = self.s[j:k]
            self.i = k
            if name in ('langle', 'rangle', 'lVert', 'rVert', 'vert', 'Vert'):
                return {'langle': '⟨', 'rangle': '⟩', 'lVert': '‖',
                        'rVert': '‖', 'vert': '|', 'Vert': '‖'}[name]
            if name in SYM:
                return SYM[name]
            raise LatexError('不支持的定界符 \\' + name)
        self.i += 1
        return c

    def _build_env(self, env, body):
        rows = [r for r in body.split('\\\\')]
        if rows and rows[-1].strip() == '':
            rows.pop()
        cells = [row.split('&') for row in rows]
        ncol = max(len(r) for r in cells) if cells else 1
        beg, end = '', ''
        if env == 'cases':
            beg, end = '{', ''
        elif env == 'pmatrix':
            beg, end = '(', ')'
        elif env == 'bmatrix':
            beg, end = '[', ']'
        elif env == 'vmatrix':
            beg, end = '|', '|'
        elif env == 'Bmatrix':
            beg, end = '{', '}'
        mpr = ('<m:mPr><m:begChr m:val="' + esc(beg) + '"/><m:endChr m:val="' +
               esc(end) + '"/><m:mcs><m:mc><m:mcPr><m:count m:val="' +
               str(ncol) + '"/><m:mcJc m:val="left"/></m:mcPr></m:mc>' +
               '</m:mcs></m:mPr>')
        out = ['<m:m>', mpr]
        for row in cells:
            out.append('<m:mr>')
            for cell in row:
                sub = Parser(cell, display=True).parse_all()
                out.append('<m:e>' + sub + '</m:e>')
            out.append('</m:mr>')
        out.append('</m:m>')
        return ''.join(out)

    def parse_command(self):
        s = self.s
        j = self.i + 1
        if j >= len(s):
            raise LatexError('孤立的反斜杠')
        if not s[j].isalpha():
            ch = s[j]
            self.i = j + 1
            two = '\\' + ch
            if two in SPACES:
                return run_xml(SPACES[two]), 'char'
            if ch in ',;:!':
                return run_xml({'\\,': '\u2009', '\\;': '\u2004',
                                '\\:': '\u2005', '\\!': ''}.get(two, '')), 'char'
            if ch == '\\':
                return '', 'char'
            if ch == ' ':
                return run_xml('\u2009'), 'char'
            if ch in '%_&$#{}':
                return run_xml(ch), 'char'
            raise LatexError('不支持的转义 \\' + ch)
        k = j
        while k < len(s) and s[k].isalpha():
            k += 1
        name = s[j:k]
        self.i = k

        if name in GREEK:
            return run_xml(GREEK[name]), 'char'
        if name in SYM:
            return run_xml(SYM[name]), 'char'
        if name in FUNCS:
            return run_xml(name, 'p'), 'func'
        if name in LIMITS:
            return run_xml(LIMIT_TEXT.get(name, name), 'p'), 'lim'
        if name in NARY:
            return NARY[name], 'nary'
        if name in SIZE_HINTS:
            return '', 'char'
        if name in ('quad', 'qquad'):
            return run_xml(SPACES['\\' + name]), 'char'
        if name in ('frac', 'dfrac', 'tfrac', 'cfrac'):
            num = self.parse_arg()
            den = self.parse_arg()
            return ('<m:f><m:num>' + num + '</m:num><m:den>' + den +
                    '</m:den></m:f>'), 'char'
        if name == 'sqrt':
            deg = ''
            self.skip_ws()
            if not self.eof() and self.s[self.i] == '[':
                self.i += 1
                deg = self.parse_seq(stop=']')
                if not self.eof() and self.s[self.i] == ']':
                    self.i += 1
                else:
                    raise LatexError('缺少 ]')
            body = self.parse_arg()
            if deg:
                return ('<m:rad><m:radPr><m:degHide m:val="0"/></m:radPr>' +
                        '<m:deg>' + deg + '</m:deg><m:e>' + body +
                        '</m:e></m:rad>'), 'char'
            return ('<m:rad><m:radPr><m:degHide m:val="1"/></m:radPr>' +
                    '<m:deg/><m:e>' + body + '</m:e></m:rad>'), 'char'
        if name in ('text', 'mathrm', 'mbox', 'textrm', 'operatorname'):
            raw = self._unescape_text(self._raw_group())
            return run_xml(raw, 'p'), 'char'
        if name in ('textbf', 'mathbf', 'bm', 'boldsymbol'):
            raw = self._unescape_text(self._raw_group())
            return run_xml(raw, 'b'), 'char'
        if name in ('underbrace', 'overbrace'):
            body = self.parse_arg()
            sub = sup = None
            self.skip_ws()
            if not self.eof() and self.s[self.i] in '_^':
                c2 = self.s[self.i]
                self.i += 1
                arg = self.parse_arg()
                if c2 == '_':
                    sub = arg
                else:
                    sup = arg
            if name == 'underbrace' and sub:
                return ('<m:limLow><m:e>' + body + '</m:e><m:lim>' + sub +
                        '</m:lim></m:limLow>'), 'char'
            if name == 'overbrace' and sup:
                return ('<m:limUpp><m:e>' + body + '</m:e><m:lim>' + sup +
                        '</m:lim></m:limUpp>'), 'char'
            return body, 'char'
        if name in ('overset', 'stackrel'):
            top = self.parse_arg()
            base = self.parse_arg()
            return ('<m:limUpp><m:e>' + base + '</m:e><m:lim>' + top +
                    '</m:lim></m:limUpp>'), 'char'
        if name == 'underset':
            bot = self.parse_arg()
            base = self.parse_arg()
            return ('<m:limLow><m:e>' + base + '</m:e><m:lim>' + bot +
                    '</m:lim></m:limLow>'), 'char'
        if name == 'mathbb':
            raw = self._raw_group().strip()
            return run_xml(MATHBB.get(raw, raw), 'p'), 'char'
        if name in ('overline', 'bar', 'underline'):
            pos = 'bot' if name == 'underline' else 'top'
            body = self.parse_arg()
            return ('<m:bar><m:barPr><m:pos m:val="' + pos + '"/></m:barPr>' +
                    '<m:e>' + body + '</m:e></m:bar>'), 'char'
        if name in ACCENT:
            body = self.parse_arg()
            return ('<m:acc><m:accPr><m:chr m:val="' + esc(ACCENT[name]) +
                    '"/></m:accPr><m:e>' + body + '</m:e></m:acc>'), 'char'
        if name == 'left':
            beg = self._delim()
            body = self.parse_seq()
            end = ''
            if self.at_cmd('right'):
                self.i += len('\\right')
                end = self._delim()
            else:
                raise LatexError('\\left 缺少配对的 \\right')
            return ('<m:d><m:dPr><m:begChr m:val="' + esc(beg) +
                    '"/><m:endChr m:val="' + esc(end) +
                    '"/><m:grow m:val="1"/></m:dPr><m:e>' + body +
                    '</m:e></m:d>'), 'char'
        if name == 'begin':
            env = self._raw_group().strip()
            if env not in ('cases', 'matrix', 'pmatrix', 'bmatrix', 'vmatrix',
                           'Bmatrix'):
                raise LatexError('不支持的环境 ' + env)
            endmark = '\\end{' + env + '}'
            idx = self.s.find(endmark, self.i)
            if idx < 0:
                raise LatexError('缺少 ' + endmark)
            body = self.s[self.i:idx]
            self.i = idx + len(endmark)
            return self._build_env(env, body), 'char'
        if name == 'end':
            raise LatexError('多余的 \\end')
        if name == 'right':
            raise LatexError('\\right 没有配对的 \\left')
        if name == 'phantom':
            self.parse_arg()
            return '', 'char'
        if name in ('displaystyle', 'limits', 'nolimits'):
            return '', 'char'
        raise LatexError('不支持的命令 \\' + name)


def omml_xml(latex, display=False):
    inner = Parser(latex, display=display).parse_all()
    if display:
        return ('<m:oMathPara ' + NSDECL +
                '><m:oMathParaPr><m:jc m:val="center"/></m:oMathParaPr>' +
                '<m:oMath>' + inner + '</m:oMath></m:oMathPara>')
    return '<m:oMath ' + NSDECL + '>' + inner + '</m:oMath>'


def omml_element(latex, display=False):
    return parse_xml(omml_xml(latex, display=display))