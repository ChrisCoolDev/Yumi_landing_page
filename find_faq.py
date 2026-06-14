import re

with open('chataigne_live.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Look for accordion, faq, question, etc.
matches = re.finditer(r'<section[^>]*id="[^"]*faq[^"]*"[^>]*>.*?</section>', content, flags=re.DOTALL | re.IGNORECASE)
found = False
for m in matches:
    print("Found FAQ section:")
    print(m.group(0)[:500])
    found = True

if not found:
    print("No section with id containing 'faq' found.")
    
    # Try just searching for 'faq' anywhere
    faq_matches = re.findall(r'.{0,50}faq.{0,50}', content, flags=re.IGNORECASE)
    for m in faq_matches:
        print(f"Match: {m}")
