#!/usr/bin/env python3
"""세계 정복(Conquer the World) 개인정보처리방침 렌더러.

정본은 같은 폴더의 content.json 이다 (10개 언어, 언어별 {name, title, effective, sections}).
  - name: 언어 이름 (상단 nav 링크와 섹션 h1 꼬리에 쓰임)
  - title: 섹션 h1 제목
  - effective: 시행일 라벨 (렌더 시 "<라벨>: <EFFECTIVE_DATE>")
  - sections: [[heading, body], ...]  번호는 렌더러가 붙인다. 본문은 일반 텍스트이며
    URL(https://...)과 이메일은 자동으로 링크가 된다. 빈 줄(\n\n)로 문단을 나눈다.

사용:
  python3 render.py            # ../privacy.html, ../privacy_ko.md 생성
  python3 render.py --md-out <path>   # 게임 저장소 docs/PRIVACY_POLICY.md 형식도 함께 생성
"""
import argparse
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = HERE.parent

APP_NAME = '세계 정복 (Conquer the World)'
PACKAGE = 'com.mkideabox.ctw'
DEVELOPER = 'mkideabox'
EMAIL = 'mkideabox.feedback@gmail.com'
EFFECTIVE_DATE = '2026-10-12'
PUBLIC_URL = 'https://rumururu.github.io/mkideabox/ctw/privacy.html'
LANGS = ['ko', 'en', 'ja', 'zh', 'es', 'fr', 'de', 'pt', 'ru', 'it']
HTML_LANG = {'zh': 'zh-Hans'}  # <section lang> 값이 언어 코드와 다른 경우

CSS = """body { font-size: 1.05rem; line-height: 1.7; margin: 0 auto; padding: 1.5rem 1rem 4rem; max-width: 46rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans KR', 'Noto Sans JP', 'Noto Sans SC', sans-serif; color: #1a1a1a; background: #fff; }
h1 { font-size: 1.55rem; line-height: 1.35; margin: 2.2em 0 .25em; }
h1:first-of-type { margin-top: 0; }
h2 { font-size: 1.15rem; margin-top: 1.6em; }
.meta { color: #666; font-size: .92rem; margin: 0 0 1.5em; }
.meta code { background: #f2f2f2; padding: .1em .35em; border-radius: 3px; }
nav { margin: 1.2em 0 2em; font-size: .95rem; display: flex; flex-wrap: wrap; gap: .4em 1em; }
section { border-top: 1px solid #e2e2e2; }
a { color: #2b5fbf; word-break: break-all; }
@media (prefers-color-scheme: dark) {
  body { background: #17181a; color: #e6e6e6; } section { border-color: #333; }
  .meta { color: #9a9a9a; } .meta code { background: #232427; } a { color: #7aa7f0; }
}"""

_LINK = re.compile(r"(https?://[A-Za-z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+|[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+)")
_TRAIL = '.,;:!?)»'


def linkify(text: str) -> str:
    """일반 텍스트를 HTML 로 이스케이프하고 URL·이메일을 <a> 로 바꾼다."""
    out, pos = [], 0
    for m in _LINK.finditer(text):
        tok = m.group(0)
        while tok and tok[-1] in _TRAIL:
            tok = tok[:-1]
        end = m.start() + len(tok)
        out.append(html.escape(text[pos:m.start()]))
        href = tok if tok.startswith('http') else 'mailto:' + tok
        out.append(f'<a href="{html.escape(href)}">{html.escape(tok)}</a>')
        pos = end
    out.append(html.escape(text[pos:]))
    return ''.join(out)


def effective(lang: dict) -> str:
    return f"{lang['effective']}: {EFFECTIVE_DATE}"


def render_html(content: dict) -> str:
    nav = ''.join(f'<a href="#{c}">{html.escape(content[c]["name"])}</a>' for c in LANGS)
    lines = [
        '<!DOCTYPE html>',
        '<html lang="ko">',
        '<head>',
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'<title>개인정보처리방침 / Privacy Policy - {APP_NAME}</title>',
        '<style>',
        CSS,
        '</style>',
        '</head>',
        '<body>',
        '<h1>개인정보처리방침 &middot; Privacy Policy</h1>',
        f'<p class="meta">{APP_NAME} &middot; <code>{PACKAGE}</code><br>',
        f'개발자 {DEVELOPER} &middot; <a href="mailto:{EMAIL}">{EMAIL}</a><br>',
        f'시행일 / Effective date: {EFFECTIVE_DATE}</p>',
        f'<nav>{nav}</nav>',
    ]
    for c in LANGS:
        lang = content[c]
        lines.append(f'<section id="{c}" lang="{HTML_LANG.get(c, c)}">')
        lines.append(f'<h1>{html.escape(lang["title"])} &middot; {html.escape(lang["name"])}</h1>')
        lines.append(f'<p class="meta">{html.escape(effective(lang))}</p>')
        for i, (heading, body) in enumerate(lang['sections'], 1):
            lines.append(f'<h2>{i}. {html.escape(heading)}</h2>')
            for para in body.split('\n\n'):
                lines.append(f'<p>{linkify(para)}</p>')
        lines.append('</section>')
    lines += ['</body>', '</html>']
    return '\n'.join(lines) + '\n'


def render_md(lang: dict, game_doc: bool) -> str:
    out = [f'# {lang["title"]} (세계 정복)', '']
    if game_doc:
        out += [f'- {effective(lang)}',
                f'- 게시 URL: {PUBLIC_URL} (10개 언어, 원본: `~/VSCodeProject/mkideabox/ctw/source/content.json`)']
    else:
        out.append(effective(lang))
    out.append('')
    for i, (heading, body) in enumerate(lang['sections'], 1):
        out += [f'## {i}. {heading}', body, '']
    return '\n'.join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--content', default=str(HERE / 'content.json'))
    ap.add_argument('--html-out', default=str(OUT_DIR / 'privacy.html'))
    ap.add_argument('--ko-md-out', default=str(OUT_DIR / 'privacy_ko.md'))
    ap.add_argument('--md-out', help='게임 저장소 docs/PRIVACY_POLICY.md 경로 (선택)')
    a = ap.parse_args()
    content = json.loads(Path(a.content).read_text(encoding='utf-8'))
    assert list(content) == LANGS, list(content)
    Path(a.html_out).write_text(render_html(content), encoding='utf-8')
    if a.ko_md_out:
        Path(a.ko_md_out).write_text(render_md(content['ko'], False), encoding='utf-8')
    if a.md_out:
        Path(a.md_out).write_text(render_md(content['ko'], True), encoding='utf-8')


if __name__ == '__main__':
    main()
