// Menú compacto para móvil. Sin JavaScript el menú se muestra completo,
// así que el contenido y la navegación nunca dependen de este archivo.
const encabezado = document.querySelector('.encabezado');
const boton = document.querySelector('.menu-boton');
const etiqueta = boton.querySelector('.sr-only');
const menu = document.querySelector('#menu-principal');

encabezado.classList.add('con-menu-compacto');
boton.hidden = false;

function abrirMenu(abierto) {
  menu.classList.toggle('abierto', abierto);
  boton.setAttribute('aria-expanded', String(abierto));
  etiqueta.textContent = abierto ? 'Cerrar menú' : 'Abrir menú';
}

boton.addEventListener('click', () => abrirMenu(!menu.classList.contains('abierto')));

menu.querySelectorAll('a').forEach((enlace) => {
  enlace.addEventListener('click', () => abrirMenu(false));
});

document.addEventListener('keydown', (evento) => {
  if (evento.key === 'Escape' && menu.classList.contains('abierto')) {
    abrirMenu(false);
    boton.focus();
  }
});
