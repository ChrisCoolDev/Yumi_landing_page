import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Cloudflare Rocket Loader modified scripts
content = re.sub(r'type="[a-f0-9]+-text/javascript"', 'type="text/javascript"', content)
content = re.sub(r'type="[a-f0-9]+-module"', 'type="module"', content)

# Remove Cloudflare analytics beacon and rocket loader script
content = re.sub(r'<!-- Cloudflare Pages Analytics -->.*?</script>', '', content, flags=re.DOTALL|re.IGNORECASE)
content = re.sub(r'<script src="/cdn-cgi/scripts/[^>]+cloudflare-static/rocket-loader.min.js"[^>]*></script>', '', content, flags=re.DOTALL)
content = re.sub(r'<script defer src=\'https://static.cloudflareinsights.com/beacon.min.js\'.*?</script>', '', content, flags=re.DOTALL)

# Remove the challenge platform script
content = re.sub(r'<script>\s*\(function\s*\(\)\s*\{.*?\}\)\(\);\s*</script>', '', content, flags=re.DOTALL)

# Remove the hidden iframe at the bottom
content = re.sub(r'<iframe\s*height="1".*?visibility:\s*hidden;.*?</iframe>', '', content, flags=re.DOTALL)

# Remove promptwatch
content = re.sub(r'<script[^>]*src="https://ingest\.promptwatch\.com[^>]*>.*?</script>', '', content, flags=re.DOTALL)

# Remove zaraz
content = re.sub(r'<script[^>]*src="/cdn-cgi/zaraz/[^>]*>.*?</script>', '', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Rocket loader and Cloudflare scripts removed.")
