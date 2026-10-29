# -*- coding: utf-8 -*-
"""서브페이지 빌드.
   index.html의 헤더·푸터·스타일·언어 전환 스크립트를 그대로 가져와 pages/*.py의 본문과 합쳐
   <slug>/index.html 을 생성한다.

   실행:  python3 build.py            (pages/ 전체)
          python3 build.py design     (특정 페이지만)
   새 페이지: pages/<slug>.py 를 suspension.py 형식으로 추가.
   빌드 후 sitemap.xml 자동 갱신.
   모델 페이지 14종은 pages/models.py (데이터: pages/_model_data.py, 가격: /models.js)."""
import re, sys, pathlib, importlib

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))

def t(ko, en, ja, zh):
    """4개 언어 data-* 속성 문자열"""
    esc = lambda s: s.replace('"', '&quot;')
    return f'data-ko="{esc(ko)}" data-en="{esc(en)}" data-ja="{esc(ja)}" data-zh="{esc(zh)}"'

def between(s, a, b):
    i = s.index(a); j = s.index(b, i)
    return s[i:j]

def load_shell():
    src = (ROOT / 'index.html').read_text(encoding='utf-8')
    head_links = between(src, '<link rel="preconnect"', '<style>')
    style = between(src, '<style>', '</style>') + '</style>'
    ticker = between(src, '<!-- ===== TICKER ===== -->', '<!-- ===== HEADER ===== -->')
    header = between(src, '<!-- ===== HEADER ===== -->', '<main id="top">')
    footer = between(src, '<!-- ===== FOOTER ===== -->', '<script>')
    js = between(src, "const IMG_BASE = 'https://", "/* ===== bikes grid ===== */")
    js = re.sub(r"/\* =+\n   MODELS.*?=+ \*/\n", "", js, flags=re.S)
    js = re.sub(r"const MODELS = \[.*?\n\];\n", "", js, flags=re.S)
    js = re.sub(r"const PRESS = \[.*?\n\];\n", "", js, flags=re.S)
    js = js.replace("  renderGrid(); renderPress(pressIdx, true);\n", "")
    js_reveal = between(src, "/* ===== reveal on scroll ===== */", "applyLang();")

    # 서브페이지에서는 메인 앵커를 /#... 로
    header = (header.replace('href="#bikes"', 'href="/#bikes"').replace('href="#moulton"', 'href="/#moulton"')
                    .replace('href="#history"', 'href="/#history"').replace('href="#buy"', 'href="/#buy"')
                    .replace('href="#top"', 'href="/"'))
    return dict(head_links=head_links, style=style, ticker=ticker, header=header, footer=footer, js=js, js_reveal=js_reveal)

def build(slug, shell):
    mod = importlib.import_module(f'pages.{slug}')
    for page in getattr(mod, 'PAGES', None) or [mod]:   # 한 모듈이 여러 페이지를 만들 수 있음 (pages/models.py)
        build_page(page, shell)

def build_page(mod, shell):
    js = re.sub(r"document\.title = \{[^\n]*\}\[LANG\];", f"document.title = {mod.TITLES_JS}[LANG];", shell['js'])
    page = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{mod.TITLE_KO}</title>
<meta name="description" content="{mod.DESCRIPTION}">
<meta property="og:title" content="{mod.OG_TITLE}">
<meta property="og:description" content="{mod.OG_DESC}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://moultonbicycles.co.kr/{mod.SLUG}/">
<link rel="canonical" href="https://moultonbicycles.co.kr/{mod.SLUG}/">
{shell['head_links']}{shell['style']}
<style>{mod.CSS}</style>
</head>
<body>

{shell['ticker']}{shell['header']}{mod.main()}
{shell['footer']}<script>
{js}
{shell['js_reveal']}applyLang();
</script>
</body>
</html>
"""
    out = ROOT / mod.SLUG / 'index.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding='utf-8')
    print('written', out.relative_to(ROOT), len(page), 'bytes')

SITE = 'https://moultonbicycles.co.kr'

def write_sitemap():
    """루트와 <폴더>/index.html 을 모두 찾아 sitemap.xml 생성. 빌드할 때마다 자동 갱신."""
    import datetime
    model_slugs = set()
    try:
        from pages._model_data import MODELS
        model_slugs = {m['slug'] for m in MODELS}
    except Exception:
        pass
    def lastmod(p):
        return datetime.datetime.fromtimestamp(p.stat().st_mtime, datetime.timezone.utc).strftime('%Y-%m-%d')
    urls = [(SITE + '/', lastmod(ROOT / 'index.html'), '1.0', 'weekly')]
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and (p / 'index.html').exists()):
        pri = '0.8' if d.name in model_slugs else '0.6'
        urls.append((f'{SITE}/{d.name}/', lastmod(d / 'index.html'), pri, 'monthly'))
    body = ''.join(f'  <url><loc>{u}</loc><lastmod>{m}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n'
                   for u, m, p, c in urls)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + '</urlset>\n'
    (ROOT / 'sitemap.xml').write_text(xml, encoding='utf-8')
    print('written sitemap.xml', len(urls), 'urls')

if __name__ == '__main__':
    shell = load_shell()
    slugs = sys.argv[1:] or [p.stem for p in (ROOT / 'pages').glob('*.py') if not p.stem.startswith('_')]
    for s in slugs:
        build(s, shell)
    write_sitemap()
