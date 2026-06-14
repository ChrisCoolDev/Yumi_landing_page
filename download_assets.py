import re
import os
import urllib.request
import urllib.parse
from html.parser import HTMLParser

base_url = "https://chataigne.ai"

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Look for typical asset patterns:
# src="/...", href="/..."
# Also url(/...) in CSS
# Also data-src="/..."

asset_patterns = [
    r'src="(/[^"]+)"',
    r'href="(/[^"]+)"',
    r'data-src="(/[^"]+)"',
    r'url\((/[^\)]+)\)'
]

assets = set()
for pattern in asset_patterns:
    matches = re.findall(pattern, content)
    for match in matches:
        # filter out absolute urls or things that are not static assets
        if match.startswith('/_nuxt/') or match.startswith('/images/') or match.startswith('/fonts/') or match.startswith('/videos/') or match.startswith('/fr/_payload.json'):
            assets.add(match)

print(f"Found {len(assets)} assets to download.")

for asset in assets:
    # remove any query strings for the file path
    asset_path = asset.split('?')[0]
    local_path = "." + asset_path
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    # some assets might have queries, we should fetch the full URL
    download_url = base_url + asset
    
    if not os.path.exists(local_path):
        print(f"Downloading {asset} -> {local_path}")
        try:
            req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
        except Exception as e:
            print(f"Failed to download {asset}: {e}")
    else:
        print(f"Already exists: {local_path}")
