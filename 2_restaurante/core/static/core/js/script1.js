
/* botón para menú desplegable */
let nav_icon = document.querySelector(".nav-boton");
let menu_nav = document.querySelector(".menu-nav");

function delegar(e) {
    menu_nav.classList.toggle("menu-nav_visible");
};

nav_icon.addEventListener("click", () => {
    menu_nav.classList.toggle("menu-nav_visible");
    // con el toggle te añade o te quita la clase menu-nav_visible a nav-boton,
    // así hace que aparezca y desaparezca. (está en la parte de añadir o quitar "class")
});

document.addEventListener("click", (e) => {
    if (e.target.matches("header ul, body div")) { 
        delegar(e);}
});


