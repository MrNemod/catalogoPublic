const menuBtn = document.getElementById("menuBtn");
const sideMenu = document.getElementById("sideMenu");
const overlay = document.getElementById("overlay");

/**
 * Función para abrir el menú lateral.
 */
const openMenu = () => {
    sideMenu.classList.remove("-translate-x-full");
    overlay.classList.remove("hidden");
    document.body.style.overflow = 'hidden';
};

/**
 * Función para cerrar el menú lateral.
 */
const closeMenu = () => {
    sideMenu.classList.add("-translate-x-full");
    overlay.classList.add("hidden");
    document.body.style.overflow = '';
};

// Evento para abrir el menú
menuBtn.onclick = openMenu;

// Evento para cerrar el menú al hacer clic en el overlay
overlay.onclick = closeMenu;