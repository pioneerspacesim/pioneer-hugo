#!/usr/bin/python
import json
import urllib.request
import markdown
with urllib.request.urlopen('https://api.github.com/repos/pioneerspacesim/pioneer/releases/latest') as json_file:
    latest = json.load(json_file)
    assets = latest['assets']
    release = latest['name']
    print('<script type="text/javascript">\n//<!CDATA[\nvar releases = {')
    for asset in assets:
        name = asset['name']
        url = asset['browser_download_url']
        date = asset['updated_at'][0:10]
        size = "{0:.2f}".format(asset['size'] / 1024 / 1024)
        if "windows" in name:
            tag = "Win"
            name = "Windows"
        elif "linux" in name:
            tag = "Lin64"
            name = "Linux 64"
        else:
            tag = "Unk"
            name = "Unknown"
        print(f'"{tag}": [ "{name}", "{release}", "{url}", "{date}", "{size} MB"],')
    print('};\n// ]]>\n</script>')

