
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Datos_Medicos import BASE_CONOCIMIENTO_MEDICO

class LLMMedico:
    def __init__(self):
        self.base_conocimiento = BASE_CONOCIMIENTO_MEDICO
        self.vectorizador = TfidfVectorizer()

        # Preparar corpus global
        self.textos = []
        self.areas = []

        for area, frases in self.base_conocimiento.items():
            for frase in frases:
                self.textos.append(frase)
                self.areas.append(area)

        self.X = self.vectorizador.fit_transform(self.textos)

    def detectar_especialidad(self, mensaje):
        mensaje_vec = self.vectorizador.transform([mensaje])
        similitudes = cosine_similarity(mensaje_vec, self.X)
        indice = similitudes.argmax()
        return self.areas[indice], indice

    def responder(self, mensaje):
        especialidad, indice = self.detectar_especialidad(mensaje)
        respuesta = self.textos[indice]

        return (
            f"🩺 Área detectada: {especialidad.replace('_', ' ').title()}\n\n"
            f"{respuesta}\n\n"
            "⚠️ Información educativa. No sustituye atención médica profesional."
        )