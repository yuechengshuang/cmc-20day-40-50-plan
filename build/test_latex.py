# -*- coding: utf-8 -*-
"""公式转换器批量自测"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from latex_omml import omml_element, LatexError

TESTS = [
    r"\lim_{x\to 0}\frac{\sin x}{x}=1",
    r"\int_0^1 x^2\,dx=\frac13",
    r"f'(x)=2x+\frac{1}{x}\quad(x>0)",
    r"f(x)=\begin{cases} x^2, & x\geq 0 \\ -x, & x<0 \end{cases}",
    r"\text{原式}=\lim_{x\to 0}\frac{1-\cos x}{x^2}",
    r"\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}",
    r"\sqrt[3]{x}+\sqrt{x^2+1}",
    r"\left(1+\frac{1}{n}\right)^n",
    r"\left.\frac{dy}{dx}\right|_{x=1}=2",
    r"\frac{\partial z}{\partial x}=y\cos(xy)",
    r"\iint_D (x+y)\,dx\,dy",
    r"\overline{z}+\vec{a}\cdot\vec{b}+\hat{x}",
    r"\forall x\in\mathbb{R},\ x^2\geq 0",
    r"a_n=\frac{1}{n}\cdot\frac{n+1}{n+2}",
    r"\lim_{n\to\infty}\sqrt[n]{n}=1",
    r"\alpha,\beta,\lambda,\mu,\varphi,\Delta,\Omega,\varepsilon",
    r"x^{n+1}+y_{n-1}+z_k^2",
    r"\int_{-\infty}^{+\infty}e^{-x^2}\,dx=\sqrt{\pi}",
    r"\ln x\leq x-1,\ \sin x<x",
    r"\frac{d^2y}{dx^2}-3\frac{dy}{dx}+2y=0",
    r"\sec^2 x+\arctan x+\csc x",
    r"|x|,\ \{a_n\},\ x\%",
    r"P(A\cup B)=\frac{1}{2}",
    r"\log_a x=\frac{\ln x}{\ln a}",
    r"\limsup_{n\to\infty}x_n,\ \max_{1\leq i\leq n}x_i",
    r"\int_0^{2\pi}\frac{dx}{5+4\cos x}=\frac{2\pi}{3}",
    r"x\to 0^-,\quad x\to 0^+",
    r"-1\leq x<1",
    r"\frac{1}{1+x^2}",
    r"\begin{cases} x+y=1 & (a) \\ x-y=3 & (b) \end{cases}",
    r"e^{x}\big|_{0}^{1}=e-1",
    r"\left[\frac{a}{b}\right]+\left\{\frac{c}{d}\right\}",
    r"\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}",
    r"\Delta y=f(x_0+\Delta x)-f(x_0)",
    r"\tan\frac{x}{2}=\frac{\sin x}{1+\cos x}",
    r"y''-y=e^x,\ y(0)=1",
    r"\lim_{x\to\infty}\left(1+\frac{a}{x}\right)^{x}=e^{a}",
]

ok = 0
bad = []
for t in TESTS:
    try:
        el = omml_element(t, display=False)
        el2 = omml_element(t, display=True)
        ok += 1
    except Exception as e:
        bad.append((t, repr(e)))

print('成功 %d / %d' % (ok, len(TESTS)))
for t, e in bad:
    print('FAIL:', t, '->', e)