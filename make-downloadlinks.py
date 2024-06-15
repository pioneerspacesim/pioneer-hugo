#!/usr/bin/python
import json
import urllib.request
import markdown
with urllib.request.urlopen('https://api.github.com/repos/pioneerspacesim/pioneer/releases/latest') as json_file:
    latest = json.load(json_file)
    assets = latest['assets']
    title = latest['name']
    body = markdown.markdown(latest['body'])
    print(f'<h4>Release: {title}</h4>')
    print('<ul>')
    for asset in assets:
        name = asset['name']
        url = asset['browser_download_url']
        date = asset['updated_at'][0:10]
        size = "{0:.2f}".format(asset['size'] / 1024 / 1024)

        label = "unknown"
        for dist in {"linux", "win", "app"}:
            if dist in name.lower():
                label = dist

        print(f'<li><a data-umami-event="Downloaded {date} ({label})" href="{url}">{name}</a> ({date} · {size} MB)</li>')
    print('</ul>')
    print(f'<p>{body}</p>')

