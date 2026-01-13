
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

class LLMMedico:
    def __init__(self):
        self.client = InferenceClient(
            model = "mistralai/Mistral-7B-Instruct",
            token = os.getenv("HF_TOKEN")
        )

    def responder(self, mensaje, especialidad="nutricion"):
        prompt = f"""
Eres un asistente médico virtual educativo para TeleSalud.

REGLAS IMPORTANTES:
- No diagnostiques enfermedades
- No recetes medicamentos
- No sustituyas a un médico
- Responde de forma clara, empática y sencilla
- Si la consulta parece grave, recomienda acudir a un profesional

Especialidad: {especialidad}

Pregunta del paciente:
{mensaje}

Respuesta médica educativa:
"""

        respuesta = self.client.text_generation(
            prompt,
            max_new_tokens = 250,
            temperature = 0.6,
            top_p = 0.9
        )

        return respuesta.strip()