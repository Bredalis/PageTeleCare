
from flask import Flask, render_template
from jinja2 import TemplateNotFound

def pagina_telecuidado():

    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/Medicina")
    def medicina():
        return render_template("Medicina.html")

    @app.route("/<nombre_especializacion>")
    def especilizacion(nombre_especializacion):
        try:
            return render_template(nombre_especializacion + ".html")
        except TemplateNotFound:
            return render_template("404.html"), 404

    @app.route("/Sobre_Nosotros")
    def sobre_nosotros():
        return render_template("Sobre_Nosotros.html")

    return app

if __name__ == "__main__":
    app = pagina_telecuidado()
    app.run()