
// Initialize Lenis for smooth scrolling
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
  touchMultiplier: 2,
  infinite: false,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}

requestAnimationFrame(raf);

// Register GSAP ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Link Lenis scroll to GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time)=>{
  lenis.raf(time * 1000)
});
gsap.ticker.lagSmoothing(0);

// Example basic entrance animations (like fading in sections)
gsap.utils.toArray('.bloc-title, .chat-item, .features-list__card, .feature-content').forEach(section => {
  gsap.fromTo(section, 
    { opacity: 0, y: 50 },
    {
      opacity: 1, 
      y: 0, 
      duration: 1,
      ease: 'power3.out',
      scrollTrigger: {
        trigger: section,
        start: 'top 85%',
      }
    }
  );
});

console.log("Vanilla JS Animations and Lenis loaded successfully!");

// FAQ Accordion Toggle Logic
document.querySelectorAll('.faq-card').forEach(card => {
  const top = card.querySelector('.faq-card__top');
  const content = card.querySelector('.faq-card__description');
  
  if (top && content) {
    // Force display block to allow height calculation
    content.style.display = 'block';
    content.style.transition = 'max-height 0.4s ease-out, opacity 0.4s ease-out, margin 0.4s ease-out';
    content.style.overflow = 'hidden';
    
    // Initially closed state
    if (!card.classList.contains('active')) {
      content.style.maxHeight = '0px';
      content.style.opacity = '0';
      content.style.marginTop = '0px';
    }

    top.addEventListener('click', () => {
      const isActive = card.classList.contains('active');
      
      // Close all others
      document.querySelectorAll('.faq-card').forEach(otherCard => {
        otherCard.classList.remove('active');
        otherCard.classList.remove('faq-card__open'); // Original CSS class
        const otherContent = otherCard.querySelector('.faq-card__description');
        if (otherContent) {
          otherContent.style.maxHeight = '0px';
          otherContent.style.opacity = '0';
          otherContent.style.marginTop = '0px';
        }
      });

      if (!isActive) {
        // Open this one
        card.classList.add('active');
        card.classList.add('faq-card__open');
        content.style.maxHeight = content.scrollHeight + 40 + 'px'; // +40 for padding safety
        content.style.opacity = '1';
        content.style.marginTop = '20px'; // Give it some breathing room if needed
      }
    });
  }
});
