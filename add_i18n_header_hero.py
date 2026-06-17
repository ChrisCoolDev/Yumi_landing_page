import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Header links
html = html.replace(
    '<a href="#solution" class="link"><span>Notre solution</span></a>',
    '<a href="#solution" class="link"><span data-i18n="nav.solution">Notre solution</span></a>'
)
html = html.replace(
    '<a href="#faq" class="link"><span>FAQ</span></a>',
    '<a href="#faq" class="link"><span data-i18n="nav.faq">FAQ</span></a>'
)
html = html.replace(
    '<a href="#contact" class="link"><span>Contactez Nous</span></a>',
    '<a href="#contact" class="link"><span data-i18n="nav.contact">Contactez Nous</span></a>'
)

# Hero section
html = html.replace(
    '<div class="line">Permettez à vos clients</div>',
    '<div class="line" data-i18n="hero.line1">Permettez à vos clients</div>'
)
html = html.replace(
    '<div class="line">de commander</div>',
    '<div class="line" data-i18n="hero.line2">de commander</div>'
)
html = html.replace(
    '<div class="line">sur WhatsApp</div>',
    '<div class="line" data-i18n="hero.line3">sur WhatsApp</div>'
)
html = html.replace(
    '<p id="home__hero-subtitle">\n              Démarquez-vous de la concurrence en offrant une expérience de\n              commande fluide, sans friction et sans aucune commission,\n              directement sur la plateforme préférée de vos clients.\n            </p>',
    '<p id="home__hero-subtitle" data-i18n="hero.desc">\n              Démarquez-vous de la concurrence en offrant une expérience de\n              commande fluide, sans friction et sans aucune commission,\n              directement sur la plateforme préférée de vos clients.\n            </p>'
)
html = html.replace(
    '<span\n                  >Essayez maintenant sur<br />sur&nbsp;<span\n                    style="display: inline"\n                    >WhatsApp</span\n                  ></span\n                >',
    '<span data-i18n="hero.button" data-i18n-html="true"\n                  >Essayez maintenant sur<br />sur&nbsp;<span\n                    style="display: inline"\n                    >WhatsApp</span\n                  ></span\n                >'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
