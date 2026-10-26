"""Verify published notice inventory, bytes, local links and release boundaries.

Standard library only; no downloads, builds, deployment or app writes.
Run from any directory: python3 scripts/verify-license-notices.py
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
DATA = PUBLIC / 'licenses/data'

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.links, self.ids = path, [], set()
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, (self.path, 'duplicate id', attrs['id'])
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])

pages = {p: Document(p) for p in PUBLIC.rglob('*.html')}
links_checked = 0
for path, document in pages.items():
    for link in document.links:
        u = urlsplit(link)
        if u.scheme or u.netloc:
            continue
        target = PUBLIC / unquote(u.path).lstrip('/') if u.path.startswith('/') else path.parent / unquote(u.path)
        if not u.path:
            target = path
        if target.is_dir():
            target = target / 'index.html'
        assert target.exists(), (path, 'missing local link', link)
        if u.fragment and target in pages:
            assert unquote(u.fragment) in pages[target].ids, (path, 'missing fragment', link)
        links_checked += 1

manifest = json.loads((DATA / 'manifest.json').read_text())
assert len(manifest) == 261
assert len({r['file'] for r in manifest}) == len(manifest)
assert {p.relative_to(DATA).as_posix() for p in DATA.rglob('*') if p.is_file() and p.name != 'manifest.json'} == {r['file'] for r in manifest}
for row in manifest:
    p = DATA / row['file']
    assert p.resolve().is_relative_to(DATA.resolve())
    b = p.read_bytes()
    assert len(b) == row['bytes'] and hashlib.sha256(b).hexdigest() == row['sha256'], row['file']
    if p.suffix == '.json':
        assert not re.search(r'/Users/|/Volumes/|BEGIN (?:EC |RSA )?PRIVATE KEY|AIza[\w-]{30}', b.decode()), row['file']

dart = json.loads((DATA / 'dart-inventory.json').read_text())
android = json.loads((DATA / 'android-inventory.json').read_text())
ios = json.loads((DATA / 'ios-inventory.json').read_text())
assert (len(dart), len(android), len(ios)) == (168, 161, 21)
for row in dart + ios:
    assert row.get('texts'), row
    if row.get('version') == '0.0.0':
        assert row['source'].startswith('https://github.com/flutter/flutter/tree/3.44.0/'), row
    for name in row['texts']:
        assert (PUBLIC / 'licenses' / name).stat().st_size, name
for row in android:
    assert row.get('effectiveLicenses') or row.get('licenses'), row
    for name in row.get('noticeFiles', []):
        assert (PUBLIC / 'licenses' / name).exists(), name
lock = (DATA / 'Podfile.lock.txt').read_text()
for row in ios:
    if row['scope'].startswith('CocoaPods'):
        assert re.search(r'^  - ' + re.escape(row['name']) + r' \(' + re.escape(row['version']) + r'\)', lock, re.M), row
hashes = json.loads((DATA / 'android-artifact-sha256.json').read_text())
assert sum(r['artifactMatch'] is True for r in hashes) == 147
assert sum(r['metadataOnly'] is True for r in hashes) == 14
assert all(r['artifactMatch'] or r['metadataOnly'] for r in hashes)
assert (DATA / 'android-flutter-NOTICES.txt').read_bytes() == (DATA / 'ios-flutter-NOTICES.txt').read_bytes()
combined = (DATA / 'native-font-NOTICES.txt').read_text()
for marker in ('SpoqaHanSansNeo', 'SIL OPEN FONT LICENSE', 'OpenSSL', 'reactive-streams', 'JSR 330'):
    assert marker in combined, marker
root = (PUBLIC / 'licenses/index.html').read_text()
es = (PUBLIC / 'licenses/es/index.html').read_text()
assert 'id="korean" lang="ko"' in root
for text in (root, es):
    for value in ('1.0.0+46', '1.0.0(45)', '168', '161', 'native-font-NOTICES.txt', 'SpoqaHanSansNeo-OFL.txt', 'android-flutter-NOTICES.txt', 'ios-flutter-NOTICES.txt'):
        assert value in text, value
    assert 'not yet verified' not in text
print(json.dumps({'status': 'PASS', 'htmlPages': len(pages), 'localLinksAndFragments': links_checked,
                  'hashedFiles': len(manifest), 'dart': len(dart), 'android': len(android), 'ios': len(ios),
                  'androidArtifactHashMatches': 147, 'androidMetadataOnly': 14}, indent=2))
