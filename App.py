
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Modelo_Medico import LLMMedico

def pagina_telecuidado():
    app = Flask(__name__)
    llm = LLMMedico()

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comentarios.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)

    class Comentario(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        especializacion = db.Column(db.String(50), nullable = False)
        nombre = db.Column(db.String(100))
        comentario = db.Column(db.Text, nullable = False)

    with app.app_context():
        db.create_all()

    # Especialidades permitidas
    ESPECIALIDADES_VALIDAS = [
        "nutricion",
        "pediatria",
        "psicologia",
        "cardiologia",
        "primeros_auxilios",
        "medicina_general",
        "ginecologia_y_obstetricia"
    ]

    def filtro_etico(mensaje):
        palabras_peligro = ["dolor pecho", "no respiro", "sangrado", "desmayo"]
        mensaje = mensaje.lower()
        for palabra in palabras_peligro:
            if palabra in mensaje:
                return "⚠️ Acude inmediatamente a un centro de salud."
        return None

    @app.route("/api/teleSalud", methods=["POST"])
    def teleSalud():
        data = request.get_json()
        mensaje = data.get("mensaje", "")

        if not mensaje:
            return jsonify({"respuesta": "Escribe una consulta válida."})

        alerta = filtro_etico(mensaje)
        if alerta:
            return jsonify({"respuesta": alerta})

        return jsonify({"respuesta": llm.responder(mensaje)})

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/sobre-nosotros")
    def sobre_nosotros():
        return render_template("Sobre_Nosotros.html")

    @app.route("/medicina")
    def medicina():
        return render_template("Medicina.html")

    @app.route("/ia")
    def ia():
        return render_template("IA.html")

    # Ruta segura para especialidades
    @app.route("/especialidad/<nombre_especializacion>")
    def especializacion(nombre_especializacion):
        ESPECIALIDADES_VALIDAS = {
            "nutricion": "Nutricion.html",
            "pediatria": "Pediatria.html",
            "psicologia": "Psicologia.html",
            "cardiologia": "Cardiologia.html",
            "primeros_auxilios": "Primeros_Auxilios.html",
            "medicina_general": "Medicina_General.html",
            "ginecologia_y_obstetricia": "Ginecologia_y_Obstetricia.html"
        }

        if nombre_especializacion not in ESPECIALIDADES_VALIDAS:
            return render_template("404.html"), 404

        comentarios = Comentario.query.filter_by(
            especializacion = nombre_especializacion
        ).all()

        return render_template(
            ESPECIALIDADES_VALIDAS[nombre_especializacion],
            comentarios = comentarios,
            especializacion = nombre_especializacion
        )

    @app.route("/comentarios", methods=["POST"])
    def guardar_comentario():
        nombre = request.form.get("nombre")
        comentario = request.form.get("comentario")
        especializacion = request.form.get("especializacion")

        if not comentario or not especializacion:
            return jsonify({"error": "Datos incompletos"}), 400

        nuevo_comentario = Comentario(
            nombre = nombre,
            comentario = comentario,
            especializacion = especializacion
        )

        db.session.add(nuevo_comentario)
        db.session.commit()

        return jsonify({"ok": True})

    @app.route("/favicon.ico")
    def favicon():
        return "", 204

    return app

if __name__ == "__main__":
    app = pagina_telecuidado()
    app.run(debug = True)