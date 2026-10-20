const menuButton = document.querySelector('.menu-toggle');
const menuLabel = menuButton.querySelector('.sr-only');
const menu = document.querySelector('#menu-principal');

function setMenu(isOpen) {
  menu.classList.toggle('open', isOpen);
  menuButton.setAttribute('aria-expanded', String(isOpen));
  menuLabel.textContent = isOpen ? 'Cerrar menú' : 'Abrir menú';
}

menuButton.addEventListener('click', () => {
  setMenu(!menu.classList.contains('open'));
});

menu.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => setMenu(false));
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menu.classList.contains('open')) {
    setMenu(false);
    menuButton.focus();
  }
});

document.querySelector('#year').textContent = new Date().getFullYear();

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
