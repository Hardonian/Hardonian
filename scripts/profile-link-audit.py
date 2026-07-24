import re, sys, urllib.request, urllib.error
from pathlib import Path
from urllib.parse import urljoin

def extract_urls(text):
    urls=[]
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)|\[[^\]]*\]\(([^)]+)\)|<(?:a|img)[^>]+(?:href|src)=["\']([^"\']+)',text):
        u=next((x for x in m.groups() if x), '')
        if u: urls.append(u.strip().split(' ')[0])
    return urls

if __name__ == '__main__':
    root=Path('.')
    text=Path('README.md').read_text()
    urls=extract_urls(text)
    fail=[]; seen=set()
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
        try:
            req=urllib.request.Request(target,headers={'User-Agent':'Hardonian-profile-audit/1.0'})
            with urllib.request.urlopen(req,timeout=20) as r:
                code=r.status
                if code >= 400 and code not in (403,429,999): fail.append((raw,code,r.headers.get('content-type','')))
                print(f'OK {code} {raw}')
        except urllib.error.HTTPError as e:
            if e.code in (403,429,999): print(f'WARN {e.code} {raw}')
            else: fail.append((raw,e.code,str(e))); print(f'FAIL {e.code} {raw}')
        except Exception as e:
            fail.append((raw,'ERROR',str(e))); print(f'FAIL ERROR {raw}: {e}')
    if fail:
        print('FAILURES',len(fail)); [print(x) for x in fail]; sys.exit(1)
    print(f'CHECKED {len(seen)} UNIQUE_LINKS_AND_IMAGES; FAILURES 0')
