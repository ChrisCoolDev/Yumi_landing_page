import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the style tag
style_match = re.search(r'<style>.*?</style>', content, flags=re.DOTALL)
style_tag = style_match.group(0) if style_match else ''

# Extract the footer tag
footer_match = re.search(r'<footer id="footer".*?</footer>', content, flags=re.DOTALL)
footer_tag = footer_match.group(0) if footer_match else ''

clean_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Footer Personnalisé</title>
    {style_tag}
    <style>
        body {{
            background-color: #fafaf9; /* keep the background color to see contrast */
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }}
    </style>
</head>
<body>
    {footer_tag}
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(clean_html)

print("Extracted footer and created a clean index.html")
