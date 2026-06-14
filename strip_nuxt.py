import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Nuxt module scripts
content = re.sub(r'<script type="module".*?</script>', '', content, flags=re.DOTALL)
content = re.sub(r'<link rel="modulepreload".*?>', '', content, flags=re.DOTALL)

# Add our own main.js script
if '<script src="/main.js"></script>' not in content:
    content = content.replace('</body>', '<script src="/main.js" type="module"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Nuxt scripts removed, added main.js")
