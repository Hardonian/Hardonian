import re
import sys
import urllib.request
import urllib.error
from pathlib import Path
from urllib.parse import urljoin
import concurrent.futures

def check_url(raw, target):
    try:
        req=urllib.request.Request(target,headers={'User-Agent':'Hardonian-profile-audit/1.0'})
        with urllib.request.urlopen(req,timeout=20) as r:
            code=r.status
            if code >= 400 and code not in (403,429,530,999):
                return ('fail', (raw,code,r.headers.get('content-type','')))
            return ('ok', f'OK {code} {raw}')
    except urllib.error.HTTPError as e:
        if e.code in (403,429,530,999):
            return ('warn', f'WARN {e.code} {raw}')
        else:
            return ('fail_err', (raw,e.code,str(e)), f'FAIL {e.code} {raw}')
    except Exception as e:
        return ('error', (raw,'ERROR',str(e)), f'FAIL ERROR {raw}: {e}')

def extract_urls(text: str) -> list[str]:
    urls = []
    pattern = r'!\[[^]]*\]\(([^)]+)\)|\[[^]]*\]\(([^)]+)\)|<(?:a|img)[^>]+(?:href|src)=["\']([^"\']+)'
    for m in re.finditer(pattern, text):
        u = next((x for x in m.groups() if x), '')
        if u:
            urls.append(u.strip().split(' ')[0])
    return urls

def resolve_local_or_target(raw: str, root: Path) -> tuple[str | None, Path | None]:
    if raw.startswith('https://') or raw.startswith('http://'):
        return raw, None

    local = (root / raw.lstrip('/')).resolve()
    if raw.startswith('/') and raw.startswith('/Hardonian/'):
        local_suffix = raw.split('/tree/main/', 1)[-1] if '/tree/main/' in raw else raw.split('/Hardonian/', 1)[-1]
        local = root / local_suffix

    if raw.startswith('products/') or raw.startswith('architecture-playbook/') or raw.startswith('assets/'):
        return None, local

    target = urljoin('https://github.com/Hardonian/Hardonian/blob/main/', raw)
    if raw.startswith('/Hardonian/'):
        target = 'https://github.com' + raw

    return target, None

def check_target(target: str, raw: str, fail: list) -> None:
    try:
        req = urllib.request.Request(target, headers={'User-Agent': 'Hardonian-profile-audit/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            code = r.status
            if code >= 400 and code not in (403, 429, 530, 999):
                fail.append((raw, code, r.headers.get('content-type', '')))
            print(f'OK {code} {raw}')
    except urllib.error.HTTPError as e:
        if e.code in (403, 429, 530, 999):
            print(f'WARN {e.code} {raw}')
        else:
            fail.append((raw, e.code, str(e)))
            print(f'FAIL {e.code} {raw}')
    except Exception as e:
        fail.append((raw, 'ERROR', str(e)))
        print(f'FAIL ERROR {raw}: {e}')

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
