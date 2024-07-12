"""
Generate changelog for latest month.
"""

#!/usr/bin/python
import collections
import re
import urllib.request
lines = []
firstline = True
changelog = urllib.request.urlopen('https://raw.githubusercontent.com/pioneerspacesim/pioneer/master/Changelog.txt').read().decode('utf-8')
for line in changelog.splitlines():
    if firstline:
        # Get title: "Month YYYY"
        lines.append((0, line.strip()))
        firstline = False
    elif len(line) == 0:
        continue
    elif line[0].isspace():
        indent = len(line) - len(line.lstrip(' '))
        content = re.sub(r'#(\d+)', r'<a href="https://github.com/pioneerspacesim/pioneer/issues/\1">#\1</a>', line.strip().lstrip(' *'))
        if content:
            lines.append((indent, content))
    else:
        break
Group = collections.namedtuple('Group', ['name', 'sections'])
Section = collections.namedtuple('Section', ['name', 'entries'])
thegroup = False
thesection = False
for line in lines:
    depth = line[0]
    content = line[1]
    if depth == 0:
        thegroup = Group(name=content, sections=[])
    if depth == 3:
        thesection = Section(name=content, entries=[])
        thegroup.sections.append(thesection)
    if depth == 5:
        thesection.entries.append(content)
print(f'For {thegroup.name}. <a href=\'https://github.com/pioneerspacesim/pioneer/blob/master/Changelog.txt\'>Full changelog</a>.')
print('<ul>')
for section in thegroup.sections:
    print(f'<li>{section.name}<ul>')
    for entry in section.entries:
        print(f'<li>{entry}</li>')
    print('</ul></li>')
print('</ul>')
