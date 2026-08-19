import re, sys, unicodedata
from pathlib import Path


def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text).strip()
    return re.sub(r'[-\s]+', '-', text)


def get_anchors(path):
    anchors = set()
    try:
        for line in Path(path).read_text(encoding='utf-8').splitlines():
            m = re.match(r'^\s{0,3}#{1,6}\s+(.*)', line)
            if m:
                text = re.sub(r'[`*_>~\[\]()]', '', m.group(1).strip())
                anchors.add(slugify(text))
    except Exception:
        pass
    return anchors


def check_repo(root):
    root = Path(root)
    errors = []
    link_re = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
    for p in sorted(root.rglob('*.md')):
        if '.git' in p.parts or 'node_modules' in p.parts:
            continue
        rel = str(p.relative_to(root))
        content = p.read_text(encoding='utf-8', errors='ignore')
        for m in link_re.finditer(content):
            target = m.group(1).strip().strip('<>')
            if ' ' in target:
                target = target.split(' ')[0]
            if not target or target.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:')):
                continue
            path_part, _, anchor = target.partition('#')
            if not path_part:
                # in-file anchor
                if anchor and slugify(anchor) not in get_anchors(p):
                    errors.append(f'{rel}: anchor not found: #{anchor}')
                continue
            found = None
            for base in (p.parent, root):
                c = base / path_part
                if c.exists():
                    found = c
                    break
                if c.is_dir() and (c / 'README.md').exists():
                    found = c / 'README.md'
                    break
            if found is None:
                errors.append(f'{rel}: broken link: {target}')
            elif anchor:
                if slugify(anchor) not in get_anchors(found):
                    errors.append(f'{rel}: broken anchor in {target}')
    return errors


for repo in sys.argv[1:]:
    errors = check_repo(repo)
    print(f'== {repo}: {len(errors)} issues')
    for e in errors:
        print('  ', e)
