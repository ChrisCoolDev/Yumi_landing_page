import re

with open('chataigne_live.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Style
style_match = re.search(r'<style>.*?</style>', content, flags=re.DOTALL)
style_tag = style_match.group(0) if style_match else ''

# Extract Header
header_match = re.search(r'<header.*?</header>', content, flags=re.DOTALL)
header_tag = header_match.group(0) if header_match else ''

# Extract footer parts
footer_top = re.search(r'<div id="footer__top">.*?</div>(?=<div id="footer__about">)', content, flags=re.DOTALL)
footer_top_html = footer_top.group(0) if footer_top else ''

footer_about = re.search(r'<div id="footer__about">.*?</div>(?=<div id="footer__bottom">)', content, flags=re.DOTALL)
footer_about_html = footer_about.group(0) if footer_about else ''

footer_bottom = re.search(r'<div id="footer__bottom">.*?</div>(?=<div class="footer__credentials">)', content, flags=re.DOTALL)
footer_bottom_html = footer_bottom.group(0) if footer_bottom else ''

footer_credentials = re.search(r'<div class="footer__credentials">.*?</div>(?=</footer>)', content, flags=re.DOTALL)
footer_credentials_html = footer_credentials.group(0) if footer_credentials else ''

# Extract FAQ
faq = re.search(r'<section id="home__faq">.*?</section>', content, flags=re.DOTALL)
faq_html = faq.group(0) if faq else ''

new_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Custom Landing Page</title>
    {style_tag}
    <style>
        body {{
            background-color: #fafaf9;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        /* Keep original footer styles by mapping them if needed, but the classes should handle most of it */
        .new-hero {{
            background-color: #152422; /* from original footer */
            color: white;
            padding-bottom: 50px;
        }}
        .new-footer {{
            background-color: #152422;
            color: white;
        }}
    </style>
</head>
<body>
    {header_tag}
    
    <!-- Hero Section (formerly footer top) -->
    <div id="footer" class="new-hero">
        {footer_top_html}
        {footer_about_html}
    </div>

    <!-- FAQ Section -->
    {faq_html}

    <!-- Actual Footer (formerly footer bottom) -->
    <footer id="footer" class="new-footer">
        {footer_bottom_html}
        {footer_credentials_html}
    </footer>

    <script src="/main.js" type="module"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML reorganized successfully")
