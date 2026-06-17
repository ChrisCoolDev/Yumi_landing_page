import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# For FAQs, we have: <h3 class="faq-card__title">
# Let's replace each one with data-i18n="faq.X.title" data-i18n-words="true"
matches = list(re.finditer(r'<h3 class="faq-card__title">', html))
for i, match in enumerate(matches):
    html = html.replace(match.group(0), f'<h3 class="faq-card__title" data-i18n="faq.{i+1}.title" data-i18n-words="true">', 1)

# For FAQ descriptions: <div class="faq-card__description">\n                <div>
matches = list(re.finditer(r'<div class="faq-card__description">\s*<div>', html))
for i, match in enumerate(matches):
    html = html.replace(match.group(0), f'<div class="faq-card__description">\n                <div data-i18n="faq.{i+1}.desc">', 1)

# Footer text
html = html.replace(
    '''<div id="footer__bottom-left">
          Châtaigne est un service qui permet aux restaurants de proposer la
          livraison et la vente à emporter via la messagerie la plus utilisée au
          monde, sans commission. Ce n'est pas un service de livraison et ne
          vend pas de produits alimentaires.
        </div>''',
    '''<div id="footer__bottom-left" data-i18n="footer.desc">
          Châtaigne est un service qui permet aux restaurants de proposer la
          livraison et la vente à emporter via la messagerie la plus utilisée au
          monde, sans commission. Ce n'est pas un service de livraison et ne
          vend pas de produits alimentaires.
        </div>'''
)

html = html.replace(
    '''<span id="footer__bottom-right__reserved"
            >© 2026 yumi, Inc.</span
          >''',
    '''<span id="footer__bottom-right__reserved" data-i18n="footer.reserved"
            >© 2026 yumi, Inc.</span
          >'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
