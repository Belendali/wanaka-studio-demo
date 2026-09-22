"""Build self-contained single-file HTML: python3 tools/build-single.py index.html wanaka-create-single-file.html"""
import base64, mimetypes, os, json, sys, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src, out = sys.argv[1], sys.argv[2]
t = open(os.path.join(ROOT, src)).read(); data = {}
for f in sorted(os.listdir(os.path.join(ROOT, 'assets'))):
    q = os.path.join(ROOT, 'assets', f)
    mt = mimetypes.guess_type(q)[0] or ('image/webp' if f.endswith('.webp') else 'application/octet-stream')
    data[f] = "data:%s;base64,%s" % (mt, base64.b64encode(open(q, 'rb').read()).decode())
old = "const A = 'assets/';\nconst U = (n) => A + n;\nconst I = (n, w, h, extra='') => `<img src=\"${A}${n}\" width=\"${w}\" height=\"${h}\" style=\"width:${w}px;height:${h}px\" alt=\"\" ${extra}>`;"
assert old in t, 'asset header not found'
inj = "const ASSETS = " + json.dumps(data) + ";\nconst A = '';\nconst U = (n) => ASSETS[n];\nconst I = (n, w, h, extra='') => `<img src=\"${ASSETS[n]}\" width=\"${w}\" height=\"${h}\" style=\"width:${w}px;height:${h}px\" alt=\"\" ${extra}>`;"
t = t.replace(old, inj)
t = re.sub(r'url\("assets/([^"]+)"\)', lambda m: 'url("' + data.get(m.group(1), '') + '")', t)
t = t.replace('href="index.html"', 'href="https://belendali.github.io/wanaka-studio-demo/"')
open(os.path.join(ROOT, out), 'w').write(t); print(out, round(os.path.getsize(os.path.join(ROOT, out)) / 1e6, 2), 'MB')
