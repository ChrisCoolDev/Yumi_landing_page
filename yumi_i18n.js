const fs = require('fs');

const indexHtmlPath = '/Users/chris/Desktop/.Code/perso/yumi/index.html';
let html = fs.readFileSync(indexHtmlPath, 'utf8');

// Add data-i18n attributes
html = html.replace(
  '<span\n              ><div class="word">Questions</div>\n              <div class="word-space">&nbsp;</div>\n              <div class="word">fréquentes</div>\n              <div class="word-space">&nbsp;</div></span\n            >',
  '<span data-i18n="faq.subtitle" data-i18n-words="true"\n              ><div class="word">Questions</div>\n              <div class="word-space">&nbsp;</div>\n              <div class="word">fréquentes</div>\n              <div class="word-space">&nbsp;</div></span\n            >'
);

html = html.replace(
  '<div class="line">\n              Nous avons répondu aux questions que vous pourriez avoir\n            </div>',
  '<div class="line" data-i18n="faq.title">\n              Nous avons répondu aux questions que vous pourriez avoir\n            </div>'
);

fs.writeFileSync(indexHtmlPath, html);
