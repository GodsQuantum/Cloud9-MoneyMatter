#!/usr/bin/env python3
from pathlib import Path
import subprocess,re,xml.etree.ElementTree as ET
p=Path(__file__).resolve().parent.parent
items=subprocess.check_output(['git','-C',str(p),'ls-files','-z']).decode().split(chr(0))
patterns=[re.compile(q,re.I) for q in ['a'+'rezki','chou'+'gar','kech'+'idi','fe'+'lla','/srv/'+'lxc/','/home/'+'arezki',r'192[.]168[.]',r'home[.]arpa',r'@gmail[.]com',r'-----BEGIN PRIVATE KEY',r'ghp_[a-zA-Z0-9]{25,}',r'github_pat_[A-Za-z0-9_]{25,}']]
bad=[]
for name in items:
 if not name or name=='scripts/privacy.py':continue
 f=p/name
 if not f.is_file() or f.stat().st_size>500_000:continue
 s=f.read_text(errors='replace')
 if any(pattern.search(s) for pattern in patterns):bad.append(name)
assert not bad,'PUBLIC_PRIVACY_REVIEW_REQUIRED '+str(sorted(set(bad)))
for name in ['docs/logo.svg','docs/oauth-flow.svg']:
 ET.parse(p/name)
print('MONEYMATTER_PUBLIC_SOURCE_PRIVACY_AND_DIAGRAMS_PASS')
