document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      const offset = 80; // Navbar height
      const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;

      window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
      });
    });
});
  
document.getElementById('encodeButton').addEventListener('click', function() {
    this.classList.add('loading');
    setTimeout(() => this.classList.remove('loading'), 1500);
});
  
document.querySelectorAll('.button').forEach(button => {
    button.addEventListener('click', function(e) {
      let ripple = document.createElement('div');
      ripple.style.position = 'absolute';
      ripple.style.background = 'rgba(255,255,255,0.4)';
      ripple.style.transform = 'translate(-50%, -50%)';
      ripple.style.pointerEvents = 'none';
      ripple.style.borderRadius = '50%';
      
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      
      ripple.style.width = ripple.style.height = `${size}px`;
      ripple.style.left = `${e.clientX - rect.left}px`;
      ripple.style.top = `${e.clientY - rect.top}px`;
      
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 1000);
    });
});