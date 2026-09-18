# -*- coding: utf-8 -*-
"""Extrae el diccionario EN de index.html a i18n/traducciones.tsv (ES<TAB>EN)."""
import io, json, re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, 'index.html')
TSV = os.path.join(ROOT, 'i18n', 'traducciones.tsv')

s = io.open(HTML, encoding='utf-8').read()
block = s.split('const EN={', 1)[1].split('\n  };', 1)[0]

rows = []
for line in block.split('\n'):
    line = line.strip().rstrip(',')
    if not line:
        continue
    m = re.match(r'^("(?:[^"\\]|\\.)*"):("(?:[^"\\]|\\.)*")$', line)
    if not m:
        raise SystemExit('linea no reconocida: ' + line[:80])
    rows.append((json.loads(m.group(1)), json.loads(m.group(2))))

with io.open(TSV, 'w', encoding='utf-8', newline='\n') as f:
    for es, en in rows:
        f.write(es.replace('\t', ' ') + '\t' + en.replace('\t', ' ') + '\n')

with io.open(os.path.join(ROOT, 'i18n', 'es.txt'), 'w', encoding='utf-8', newline='\n') as f:
    for es, en in rows:
        f.write(es + '\n')

print('%d filas -> %s (+ i18n/es.txt)' % (len(rows), TSV))
