let lastScrollTop = 0;
const header = document.getElementById('header');
const footer = document.getElementById('footer'); // Selecciona el pie de página

window.addEventListener('scroll', function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    let viewportHeight = window.innerHeight; // Altura visible de la ventana
    let pageHeight = document.documentElement.scrollHeight; // Altura total de la página

    // Oculta el header mientras haces scroll hacia abajo
    if (scrollTop > lastScrollTop) {
        header.classList.add('hidden');
    } else {
        header.classList.remove('hidden');
    }

    // Muestra el footer solo si estás al final de la página
    if (scrollTop + viewportHeight >= pageHeight) {
        footer.classList.remove('hidden'); // Muestra el pie de página
    } else {
        footer.classList.add('hidden'); // Oculta el pie de página
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // Evitar valores negativos
});
