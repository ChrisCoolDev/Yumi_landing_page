#!/usr/bin/env python3
"""
Update FAQ and footer content to reflect the actual Yumi application.
Based on analysis of /Users/chris/Desktop/.Code/perso/whatsapp-automation
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── Helper: build word-div structure from text ─────────────────────────
def words_to_divs(text):
    words = text.split(' ')
    parts = []
    for i, word in enumerate(words):
        parts.append(f'<div class="word">{word}</div>')
        parts.append('<div class="word-space">&nbsp;</div>')
    return '\n                   '.join(parts)

# ─── New FAQ data (Yumi-specific, based on the real app) ────────────────
faqs = [
    {
        "title_fr": "Qu'est-ce que Yumi ?",
        "desc_fr": "Yumi est un assistant WhatsApp intelligent alimenté par l'IA, conçu pour les commerçants locaux au Cameroun. Il permet à vos clients de passer des commandes directement par message texte ou vocal sur WhatsApp. L'IA accueille vos clients, présente votre catalogue de produits, prend les commandes et calcule automatiquement les totaux en FCFA.",
    },
    {
        "title_fr": "Comment mes clients passent-ils commande ?",
        "desc_fr": "C'est très simple ! Vos clients envoient un message au numéro WhatsApp dédié de votre commerce. L'IA les accueille, leur propose le menu, et ils peuvent commander en langage naturel — par exemple \"Je veux 2 burgers et un Fanta\". L'IA comprend le français et l'anglais, et peut même traiter les messages vocaux. Aucune application à télécharger, aucune inscription requise.",
    },
    {
        "title_fr": "Quels moyens de paiement sont acceptés ?",
        "desc_fr": "Yumi supporte les paiements par Mobile Money (MTN MoMo et Orange Money) directement dans la conversation WhatsApp, ainsi que le paiement en espèces à la livraison. Le paiement Mobile Money est sécurisé via NotchPay — un pop-up s'affiche sur le téléphone du client pour confirmer la transaction.",
    },
    {
        "title_fr": "Comment fonctionne la livraison ?",
        "desc_fr": "Yumi intègre un système complet de gestion des livraisons. Quand une commande est confirmée, le commerçant est notifié et peut assigner un livreur. Le client reçoit des notifications en temps réel à chaque étape : préparation, livreur assigné, en route, arrivé, et livré. Les livreurs gèrent leurs courses directement via WhatsApp aussi.",
    },
    {
        "title_fr": "Combien coûte Yumi ?",
        "desc_fr": "Yumi utilise un modèle de tarification transparent. Vous gardez 100% de vos revenus de commandes — sans aucune commission. Contactez-nous pour connaître nos formules d'abonnement adaptées à votre volume de commandes.",
    },
    {
        "title_fr": "L'IA comprend-elle les demandes spéciales ?",
        "desc_fr": "Oui ! Notre IA conversationnelle est conçue spécifiquement pour la prise de commande. Elle comprend les demandes en français et en anglais, traite les messages vocaux, et gère les commandes complexes comme \"sans oignons\" ou \"sauce à part\". Elle s'adapte automatiquement à la langue du client dès son premier message.",
    },
    {
        "title_fr": "Comment mettre à jour mon catalogue ?",
        "desc_fr": "Vous pouvez gérer votre catalogue produits, vos catégories, vos prix et la disponibilité des articles via le tableau de bord d'administration de Yumi. L'IA apprend instantanément vos modifications et arrête de recommander les articles en rupture de stock.",
    },
    {
        "title_fr": "Pourquoi WhatsApp ?",
        "desc_fr": "WhatsApp est l'application de messagerie la plus utilisée au Cameroun et en Afrique. Tout le monde sait envoyer un message, mais tout le monde ne sait pas naviguer dans une application de commande. Avec Yumi, pas besoin de télécharger une nouvelle app — vos clients commandent sur la plateforme qu'ils utilisent déjà au quotidien.",
    },
    {
        "title_fr": "Yumi gère-t-il plusieurs commerces ?",
        "desc_fr": "Oui ! Yumi est conçu en architecture multi-commerçants. Chaque commerce dispose de son propre numéro WhatsApp, de son catalogue personnalisé, de ses zones de livraison avec tarification par zone, et de son équipe de livreurs. Tout est géré indépendamment.",
    },
    {
        "title_fr": "Comment m'inscrire ?",
        "desc_fr": "Cliquez sur \"Essayez maintenant sur WhatsApp\" pour tester le bot directement. Pour configurer Yumi pour votre commerce, contactez-nous via le formulaire sur cette page. Nous vous accompagnerons dans la mise en place de votre catalogue, vos zones de livraison et votre numéro WhatsApp dédié.",
    },
]

# ─── Build new FAQ HTML ─────────────────────────────────────────────────
faq_cards = []
for i, faq in enumerate(faqs, 1):
    title_words = words_to_divs(faq['title_fr'])
    card = f'''            <div class="faq-card">
              <div class="faq-card__top">
                <div class="faq-card__toggle">
                  <span></span><span></span>
                  <div class="faq-card__toggle-under"></div>
                </div>
                <h3 class="faq-card__title" data-i18n="faq.{i}.title" data-i18n-words="true">
                   {title_words}
                </h3>
              </div>
              <div class="faq-card__description">
                <div data-i18n="faq.{i}.desc">
                  {faq['desc_fr']}
                </div>
              </div>
            </div>'''
    faq_cards.append(card)

new_faq_html = '\n'.join(faq_cards)

# ─── Replace FAQ section ────────────────────────────────────────────────
# Find the faq-list div and replace its content
faq_pattern = r'(<div id="faq-list">\s*<!--\[-->\s*)(.*?)(<!--\]-->\s*</div>)'
replacement = r'\g<1>\n' + new_faq_html + r'\n            \g<3>'
html = re.sub(faq_pattern, replacement, html, flags=re.DOTALL)

# ─── Update footer description ──────────────────────────────────────────
old_footer = '''Châtaigne est un service qui permet aux restaurants de proposer la
          livraison et la vente à emporter via la messagerie la plus utilisée au
          monde, sans commission. Ce n'est pas un service de livraison et ne
          vend pas de produits alimentaires.'''
new_footer = '''Yumi est un assistant WhatsApp IA qui permet aux commerçants locaux au
          Cameroun de recevoir et gérer des commandes directement via WhatsApp,
          sans commission. Paiement par Mobile Money et espèces. Ce n'est pas
          un service de livraison.'''
html = html.replace(old_footer, new_footer)

# ─── Update footer AI section (Châtaigne → Yumi) ────────────────────────
html = html.replace("Demandez à l&#39;IA", "Demandez à l&#39;IA")
html = html.replace("Ask ChatGPT about Châtaigne", "Ask ChatGPT about Yumi")
html = html.replace("Ask Claude about Châtaigne", "Ask Claude about Yumi")
html = html.replace("Ask Perplexity about Châtaigne", "Ask Perplexity about Yumi")
html = html.replace("Ask Gemini about Châtaigne", "Ask Gemini about Yumi")
html = html.replace("Ask Grok about Châtaigne", "Ask Grok about Yumi")

# Update the AI query URLs to be about Yumi
old_query = "En%20tant%20que%20restaurateur%2C%20je%20veux%20comprendre%20comment%20fonctionne%20Ch%C3%A2taigne%20(chataigne.ai)"
new_query = "En%20tant%20que%20commer%C3%A7ant%20au%20Cameroun%2C%20je%20veux%20comprendre%20comment%20fonctionne%20Yumi%2C%20l%27assistant%20WhatsApp%20IA"
html = html.replace(old_query, new_query)

old_rest = "1.%20Comment%20mes%20clients%20passent-ils%20commande%20via%20WhatsApp%20%3F%0A2.%20Comment%20je%20re%C3%A7ois%20et%20g%C3%A8re%20les%20commandes%20%3F%0A3.%20Que%20montre%20le%20tableau%20de%20bord%20%3F%0A4.%20Quels%20sont%20les%20co%C3%BBts%20par%20rapport%20%C3%A0%20Uber%20Eats%2FDeliveroo%20%3F%0A5.%20Combien%20de%20temps%20pour%20d%C3%A9marrer%20%3F%0A%0AExpliquez%20simplement%2C%20comme%20si%20vous%20d%C3%A9criviez%20l"
new_rest = "1.%20Comment%20mes%20clients%20commandent-ils%20via%20WhatsApp%20%3F%0A2.%20Quels%20moyens%20de%20paiement%20(MTN%20MoMo%2C%20Orange%20Money)%20%3F%0A3.%20Comment%20g%C3%A9rer%20les%20livraisons%20%3F%0A4.%20Combien%20%C3%A7a%20co%C3%BBte%20%3F%0A5.%20Comment%20d%C3%A9marrer%20%3F%0A%0AExpliquez%20simplement%2C%20comme%20si%20vous%20d%C3%A9criviez%20l"
html = html.replace(old_rest, new_rest)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ FAQ and footer content updated successfully!")
print(f"   - {len(faqs)} FAQ items written")
print("   - Footer description updated for Yumi")
print("   - AI links updated for Yumi")
