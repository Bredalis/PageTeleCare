
// Ocultar el índice de contenido al estar sobre el footer
document.addEventListener("scroll", function() {
    const enlaces = document.querySelector(".contenido-enlaces");
    const footer = document.querySelector("footer");
    const footerTop = footer.getBoundingClientRect().top;
    const enlacesHeight = enlaces.offsetHeight;

    footerTop < window.innerHeight ? enlaces.style.opacity = "0" : enlaces.style.opacity = "1";
});