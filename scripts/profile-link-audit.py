import re, sys, urllib.request, urllib.error
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

def audit():
    root=Path('.')
    text=Path('README.md').read_text()
    urls=[]
    for m in re.finditer(r'!\[[^]]*\]\(([^)]+)\)|\[[^]]*\]\(([^)]+)\)|<(?:a|img)[^>]+(?:href|src)=["\']([^"\']+)',text):
        u=next((x for x in m.groups() if x), '')
        if u: urls.append(u.strip().split(' ')[0])
    fail=[]; seen=set(); to_check=[]
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
        futures = {executor.submit(check_url, raw, target): raw for raw, target in to_check}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res[0] == 'fail': fail.append(res[1])
            elif res[0] == 'ok': print(res[1])
            elif res[0] == 'warn': print(res[1])
            elif res[0] == 'fail_err': fail.append(res[1]); print(res[2])
            elif res[0] == 'error': fail.append(res[1]); print(res[2])

    if fail:
        print('FAILURES',len(fail)); [print(x) for x in fail]; sys.exit(1)
    print(f'CHECKED {len(seen)} UNIQUE_LINKS_AND_IMAGES; FAILURES 0')

if __name__ == '__main__':
    audit()
