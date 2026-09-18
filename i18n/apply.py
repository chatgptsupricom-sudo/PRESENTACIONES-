# -*- coding: utf-8 -*-
"""Reinyecta i18n/traducciones.tsv (ES<TAB>EN) en el diccionario EN de index.html."""
import io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, 'index.html')
TSV = os.path.join(ROOT, 'i18n', 'traducciones.tsv')

pairs = []
for i, line in enumerate(io.open(TSV, encoding='utf-8'), 1):
    line = line.rstrip('\n').rstrip('\r')
    if not line.strip():
        continue
    if '\t' not in line:
        raise SystemExit('linea %d sin TAB: %s' % (i, line[:80]))
    es, en = line.split('\t', 1)
    pairs.append((es, en))

body = '\n'.join(
    json.dumps(es, ensure_ascii=False) + ':' + json.dumps(en, ensure_ascii=False) + ','
    for es, en in pairs
)
body = body.rstrip(',')

s = io.open(HTML, encoding='utf-8').read()
head, rest = s.split('const EN={', 1)
old, tail = rest.split('\n  };', 1)
io.open(HTML, 'w', encoding='utf-8').write(head + 'const EN={\n' + body + '\n  };' + tail)

print('%d traducciones aplicadas a index.html' % len(pairs))
