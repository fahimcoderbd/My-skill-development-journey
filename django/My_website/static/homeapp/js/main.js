const menuButton = document.querySelector('#menuButton');
const navMenu = document.querySelector('#navMenu');

if (menuButton && navMenu) {
  menuButton.addEventListener('click', () => {
    const expanded = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!expanded));
    navMenu.classList.toggle('hidden');
  });
}

const floatShapes = document.querySelectorAll('[data-float]');

if (floatShapes.length) {
  document.addEventListener('mousemove', (event) => {
    const x = (event.clientX / window.innerWidth - 0.5) * 20;
    const y = (event.clientY / window.innerHeight - 0.5) * 20;

    floatShapes.forEach((shape) => {
      const speed = parseFloat(shape.dataset.float) || 0.6;
      shape.style.transform = `translate3d(${x * speed}px, ${y * speed}px, 0)`;
    });
  });
}
