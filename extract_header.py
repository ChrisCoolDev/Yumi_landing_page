import re

with open('temp_index.html', 'r', encoding='utf-8') as f:
    temp_content = f.read()

# Extract the header tag
header_match = re.search(r'<header.*?</header>', temp_content, flags=re.DOTALL)
if header_match:
    header_tag = header_match.group(0)
else:
    print("Header not found")
    header_tag = ""

with open('index.html', 'r', encoding='utf-8') as f:
    local_content = f.read()

# Inject header inside body, before footer
# Look for <body> tag
if header_tag:
    local_content = re.sub(r'(<body>)', r'\1\n' + header_tag, local_content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(local_content)
    print("Header extracted and added to index.html")
