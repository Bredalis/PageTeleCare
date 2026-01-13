
from flask import Flask, render_template, request, jsonify
from jinja2 import TemplateNotFound
from Modelo_Medico import LLMMedico

def pagina_telecuidado():
    app = Flask(__name__)
    llm = LLMMedico()

    def filtro_etico(mensaje):
        palabras_peligro = ["dolor pecho", "no respiro", "sangrado", "desmayo"]
        mensaje_lower = mensaje.lower()

        for palabra in palabras_peligro:
            if palabra in mensaje_lower:
                return (
                    "⚠️ Tu consulta puede ser urgente. "
                    "Por favor acude inmediatamente a un centro de salud."
                )
        return None

    @app.route("/api/teleSalud", methods=["POST"])
    def teleSalud():
        data = request.get_json()
        mensaje = data.get("mensaje")
        especialidad = data.get("especialidad", "nutricion")

        alerta = filtro_etico(mensaje)
        if alerta:
            return jsonify({"respuesta": alerta})

        respuesta = llm.responder(mensaje, especialidad)
        return jsonify({"respuesta": respuesta})

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/medicina")
    def medicina():
        return render_template("Medicina.html")

    @app.route("/ia")
    def ia():
        return render_template("IA.html")

    @app.route("/<nombre_especializacion>")
    def especilizacion(nombre_especializacion):
        try:
            return render_template(f"{nombre_especializacion}.html")
        except TemplateNotFound:
            return render_template("404.html"), 404

    @app.route("/sobre-nosotros")
    def sobre_nosotros():
        return render_template("Sobre_Nosotros.html")

    return app

if __name__ == "__main__":
    app = pagina_telecuidado()
    app.run()