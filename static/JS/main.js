
// Ocultar el índice de contenido al estar sobre el footer
document.addEventListener("scroll", function() {
    const enlaces = document.querySelector(".contenido-enlaces");
    const footer = document.querySelector("footer");
    const footerTop = footer.getBoundingClientRect().top;
    const enlacesHeight = enlaces.offsetHeight;

    footerTop < window.innerHeight ? enlaces.style.opacity = "0" : enlaces.style.opacity = "1";
});

// Enviar mensajes al modelo
function enviarMensaje() {
    const input = document.getElementById("userInput");
    const texto = input.value.trim();

    if (texto === "") return;

    agregarMensaje(texto, "usuario");
    input.value = "";

    fetch("/api/teleSalud", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            mensaje: texto
        })
    })
    .then(res => res.json())
    .then(data => {
        agregarMensaje(data.respuesta, "bot");
    })
    .catch(error => {
        console.error("Error:", error);
        agregarMensaje("Hubo un error al procesar tu consulta.", "bot");
    });
}

function agregarMensaje(texto, tipo) {
    const chat = document.getElementById("chat-window");
    const msg = document.createElement("div");
    msg.classList.add("mensaje", tipo);
    msg.textContent = texto;
    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
}

// Enviar comentarios al archivo App.py
document.getElementById("form-comentarios").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    await fetch("/comentarios", {
        method: "POST",
        body: formData
    });

    location.reload();
});