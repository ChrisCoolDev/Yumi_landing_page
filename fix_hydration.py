import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace payload URLs
content = content.replace('"/fr/_payload.json', '"/_payload.json')

# Replace the Nuxt route hydration path
content = content.replace('"/fr/",\n        1779801157418', '"/",\n        1779801157418')
# Or if it was just "/fr/"
content = re.sub(r'"/fr/",(\s*\d+)', r'"/",\1', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated hydration routes in index.html")
