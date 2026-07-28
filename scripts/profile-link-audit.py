import re, sys, urllib.request, urllib.error
from pathlib import Path
from urllib.parse import urljoin

def extract_urls(text):
    urls = []
    pattern = r'!\[[^]]*\]\(([^)]+)\)|\[[^]]*\]\(([^)]+)\)|<(?:a|img)[^>]+(?:href|src)=["\']([^"\']+)'
    for m in re.finditer(pattern, text):
        u = next((x for x in m.groups() if x), '')
        if u:
            urls.append(u.strip().split(' ')[0])
    return urls

def get_local_path(raw, root):
    local = (root / raw.lstrip('/')).resolve()
    if raw.startswith('/') and raw.startswith('/Hardonian/'):
        if '/tree/main/' in raw:
            local = root / raw.split('/tree/main/', 1)[-1]
        else:
            local = root / raw.split('/Hardonian/', 1)[-1]
    return local

def is_local_only(raw):
    return raw.startswith('products/') or raw.startswith('architecture-playbook/') or raw.startswith('assets/')

def get_target_url(raw):
    if raw.startswith('https://') or raw.startswith('http://'):
        return raw

    target = urljoin('https://github.com/Hardonian/Hardonian/blob/main/', raw)
    if raw.startswith('/Hardonian/'):
        target = 'https://github.com' + raw
    return target

def check_url(target, raw):
    req = urllib.request.Request(target, headers={'User-Agent': 'Hardonian-profile-audit/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            code = r.status
            if code >= 400 and code not in (403, 429, 530, 999):
                return (raw, code, r.headers.get('content-type', ''))
            print(f'OK {code} {raw}')
    except urllib.error.HTTPError as e:
        if e.code in (403, 429, 530, 999):
            print(f'WARN {e.code} {raw}')
        else:
            print(f'FAIL {e.code} {raw}')
            return (raw, e.code, str(e))
    except Exception as e:
        print(f'FAIL ERROR {raw}: {e}')
        return (raw, 'ERROR', str(e))
    return None

def audit():
    root = Path('.')
    text = Path('README.md').read_text()
    urls = extract_urls(text)

    fail = []
    seen = set()

    for raw in urls:
        if raw in seen or raw.startswith('#'):
            continue
        seen.add(raw)

        if raw.startswith('mailto:'):
            continue

        if not (raw.startswith('https://') or raw.startswith('http://')):
            local = get_local_path(raw, root)
            if is_local_only(raw):
                if not local.exists():
                    fail.append((raw, 'LOCAL_MISSING', str(local)))
                else:
                    print(f'LOCAL 200 {raw}')
                continue

        target = get_target_url(raw)

        error = check_url(target, raw)
        if error:
            fail.append(error)

    if fail:
        print('FAILURES', len(fail))
        for x in fail:
            print(x)
        sys.exit(1)

    print(f'CHECKED {len(seen)} UNIQUE_LINKS_AND_IMAGES; FAILURES 0')

if __name__ == '__main__':
    audit()
