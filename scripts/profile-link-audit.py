import re, sys, urllib.request, urllib.error
import concurrent.futures
from pathlib import Path
from urllib.parse import urljoin
root=Path('.')
text=Path('README.md').read_text()
urls=[]
for m in re.finditer(r'!\[[^]]*\]\(([^)]+)\)|\[[^]]*\]\(([^)]+)\)|<(?:a|img)[^>]+(?:href|src)=["\']([^"\']+)',text):
    u=next((x for x in m.groups() if x), '')
    if u: urls.append(u.strip().split(' ')[0])
fail=[]; seen=set()
to_check=[]

def fetch(args):
    raw, target = args
    try:
        req=urllib.request.Request(target,headers={'User-Agent':'Hardonian-profile-audit/1.0'})
        with urllib.request.urlopen(req,timeout=20) as r:
            return (raw, 'OK', r.status, r.headers.get('content-type',''))
    except urllib.error.HTTPError as e:
        return (raw, 'HTTPError', e.code, str(e))
    except Exception as e:
        return (raw, 'ERROR', 'ERROR', str(e))

for raw in urls:
    if raw in seen or raw.startswith('#'): continue
    seen.add(raw)
    if raw.startswith('mailto:'): continue
    if raw.startswith('https://') or raw.startswith('http://'):
        target=raw
    else:
        local=(root/raw.lstrip('/')).resolve()
        if raw.startswith('/') and raw.startswith('/Hardonian/'):
            local=root/(raw.split('/tree/main/',1)[-1] if '/tree/main/' in raw else raw.split('/Hardonian/',1)[-1])
        if raw.startswith('products/') or raw.startswith('architecture-playbook/') or raw.startswith('assets/'):
            if not local.exists(): fail.append((raw,'LOCAL_MISSING',str(local))); continue
            print(f'LOCAL 200 {raw}')
            continue
        target=urljoin('https://github.com/Hardonian/Hardonian/blob/main/', raw)
        if raw.startswith('/Hardonian/'):
            target='https://github.com'+raw
    to_check.append((raw, target))

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for raw, status, code, extra in executor.map(fetch, to_check):
        if status == 'OK':
            if code >= 400 and code not in (403,429,999): fail.append((raw,code,extra))
            print(f'OK {code} {raw}')
        elif status == 'HTTPError':
            if code in (403,429,999): print(f'WARN {code} {raw}')
            else: fail.append((raw,code,extra)); print(f'FAIL {code} {raw}')
        else:
            fail.append((raw,code,extra)); print(f'FAIL ERROR {raw}: {extra}')

if fail:
    print('FAILURES',len(fail)); [print(x) for x in fail]; sys.exit(1)
print(f'CHECKED {len(seen)} UNIQUE_LINKS_AND_IMAGES; FAILURES 0')
