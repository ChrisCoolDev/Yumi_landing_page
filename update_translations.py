import re

with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_translations = """const translations = {
  fr: {
    "nav.solution": "Notre solution",
    "nav.faq": "FAQ",
    "nav.contact": "Contactez Nous",
    "hero.line1": "Permettez à vos clients",
    "hero.line2": "de commander",
    "hero.line3": "sur WhatsApp",
    "hero.desc": "Démarquez-vous de la concurrence en offrant une expérience de commande fluide, sans friction et sans aucune commission, directement sur la plateforme préférée de vos clients.",
    "hero.button": "Essayez maintenant sur<br />sur&nbsp;<span style=\\"display: inline\\">WhatsApp</span>",
    "faq.subtitle": "Questions fréquentes",
    "faq.title": "Nous avons répondu aux questions que vous pourriez avoir",
    "faq.1.title": "Qu'est-ce que Châtaigne ?",
    "faq.1.desc": "Châtaigne est une plateforme de commande WhatsApp alimentée par l'IA pour les restaurants. Elle permet aux clients de passer des commandes de nourriture par messages texte ou vocaux sur WhatsApp, avec des commandes qui arrivent directement dans votre système de caisse existant. Chaque restaurant reçoit un numéro WhatsApp dédié comme canal de commande direct—aucun téléchargement d'application requis pour les clients.",
    "faq.2.title": "Combien coûte Châtaigne ?",
    "faq.2.desc": "Châtaigne facture des frais mensuels fixes sans aucune commission par commande. L'abonnement comprend toutes les fonctionnalités de l'IA de commande, un numéro de téléphone dédié et l'accès au tableau de bord. Contactez-nous pour une tarification détaillée.",
    "faq.3.title": "Les clients doivent-ils télécharger une application ?",
    "faq.3.desc": "Absolument pas ! Tout se passe directement sur WhatsApp. Les clients enregistrent le numéro de votre restaurant et envoient un message pour commander, comme ils le feraient avec un ami. Ce processus sans friction entraîne des taux de conversion plus élevés que le téléchargement d'une application à chaque fois—pas besoin d'inscription. Il est très utile de partager le numéro sur Google Maps ou Instagram.",
    "faq.4.title": "L'IA peut-elle gérer les demandes spéciales ?",
    "faq.4.desc": "Oui, notre IA conversationnelle est conçue spécifiquement pour la prise de commande de nourriture. Elle peut comprendre des demandes complexes comme \\"sans oignons\\", \\"sauce à part\\" ou des modifications diététiques tout en s'assurant qu'elles correspondent à ce qui est possible avec les éléments de votre menu.",
    "faq.5.title": "Comment mettre à jour mon menu ?",
    "faq.5.desc": "Vous pouvez facilement mettre à jour votre menu, vos prix et la disponibilité des articles en temps réel via notre tableau de bord commerçant. L'IA apprend instantanément vos nouvelles offres de menu et arrêtera de recommander les articles que vous marquez comme en rupture de stock.",
    "faq.6.title": "Pourquoi devrais-je choisir Châtaigne plutôt qu'UberEats, DoorDash, etc. ?",
    "faq.6.desc": "Vous ne devriez pas ! Châtaigne fonctionne mieux lorsqu'il est utilisé avec d'autres applications de livraison de nourriture. Cela vous permet d'extraire une meilleure marge de vos clients récurrents, qui représentent presque toujours la plus grande partie de votre entreprise.",
    "footer.desc": "Châtaigne est un service qui permet aux restaurants de proposer la livraison et la vente à emporter via la messagerie la plus utilisée au monde, sans commission. Ce n'est pas un service de livraison et ne vend pas de produits alimentaires.",
    "footer.reserved": "© 2026 yumi, Inc."
  },
  en: {
    "nav.solution": "Our solution",
    "nav.faq": "FAQ",
    "nav.contact": "Contact Us",
    "hero.line1": "Allow your customers",
    "hero.line2": "to order",
    "hero.line3": "on WhatsApp",
    "hero.desc": "Stand out from the competition by offering a smooth, frictionless, and zero-commission ordering experience, directly on your customers' favorite platform.",
    "hero.button": "Try now on<br />on&nbsp;<span style=\\"display: inline\\">WhatsApp</span>",
    "faq.subtitle": "Frequently Asked Questions",
    "faq.title": "We have answered the questions you might have",
    "faq.1.title": "What is Châtaigne?",
    "faq.1.desc": "Châtaigne is an AI-powered WhatsApp ordering platform for restaurants. It allows customers to place food orders via text or voice messages on WhatsApp, with orders arriving directly in your existing POS system. Each restaurant gets a dedicated WhatsApp number as a direct ordering channel—no app download required for customers.",
    "faq.2.title": "How much does Châtaigne cost?",
    "faq.2.desc": "Châtaigne charges a fixed monthly fee with zero per-order commissions. The subscription includes all AI ordering features, a dedicated phone number, and dashboard access. Contact us for detailed pricing.",
    "faq.3.title": "Do customers need to download an app?",
    "faq.3.desc": "Absolutely not! Everything happens directly on WhatsApp. Customers save your restaurant's number and send a message to order, just like they would with a friend. This frictionless process leads to higher conversion rates than downloading an app every time—no registration required. It's very useful to share the number on Google Maps or Instagram.",
    "faq.4.title": "Can the AI handle special requests?",
    "faq.4.desc": "Yes, our conversational AI is designed specifically for food ordering. It can understand complex requests like \\"no onions\\", \\"sauce on the side\\" or dietary modifications while ensuring they match what's possible with your menu items.",
    "faq.5.title": "How do I update my menu?",
    "faq.5.desc": "You can easily update your menu, prices, and item availability in real time via our merchant dashboard. The AI instantly learns your new menu offerings and will stop recommending items you mark as out of stock.",
    "faq.6.title": "Why should I choose Châtaigne over UberEats, DoorDash, etc.?",
    "faq.6.desc": "You shouldn't! Châtaigne works best when used with other food delivery apps. It allows you to extract a better margin from your recurring customers, who almost always make up the biggest part of your business.",
    "footer.desc": "Châtaigne is a service that allows restaurants to offer delivery and takeout via the world's most used messaging app, commission-free. It is not a delivery service and does not sell food products.",
    "footer.reserved": "© 2026 yumi, Inc."
  }
};"""

js = re.sub(r'const translations = \{.*?\n\};\n', new_translations + '\n', js, flags=re.DOTALL)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)
