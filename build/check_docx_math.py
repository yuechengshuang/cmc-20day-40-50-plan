# -*- coding: utf-8 -*-
"""检查生成的 docx：统计 Word 原生公式数量、表格数、段落数，
并查找是否有原始 LaTeX 漏进正文（说明公式转换失败走了兜底）。
用法：python check_docx_math.py <docx路径>
"""
import re
import sys
import zipfile

path = sys.argv[1]
with zipfile.ZipFile(path) as z:
    xml = z.read('word/document.xml').decode('utf-8')

n_omath = len(re.findall(r'<m:oMath[ >]', xml))
n_omathpara = len(re.findall(r'<m:oMathPara[ >]', xml))
n_frac = len(re.findall(r'<m:f>', xml))
n_nary = len(re.findall(r'<m:nary>', xml))
n_rad = len(re.findall(r'<m:rad>', xml))
n_d = len(re.findall(r'<m:d>', xml))
n_tbl = len(re.findall(r'<w:tbl>', xml))
n_par = len(re.findall(r'<w:p[ >]', xml))
n_bad = len(re.findall(r'<m:oMath>', xml))

# 漏网的 LaTeX：正文文本里出现 \frac \lim \int \sum 等
texts = re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>', xml, re.S)
leak = []
for t in texts:
    if re.search(r'\\[a-zA-Z]{2,}', t):
        leak.append(t[:100])

print('文件：%s' % path)
print('  段落数            %d' % n_par)
print('  表格数            %d' % n_tbl)
print('  行内公式 oMath    %d' % n_omath)
print('  独立公式 oMathPara %d' % n_omathpara)
print('  分式 %d，根式 %d，积分/求和 nary %d，括号对 %d'
      % (n_frac, n_rad, n_nary, n_d))
print('  正文里残留的 LaTeX：%d 处' % len(leak))
for t in leak[:10]:
    print('     ! %s' % t)
print('  判定：%s' % ('全部公式已转为 Word 原生公式'
                   if not leak else '存在未转换公式（已用原文兜底）'))