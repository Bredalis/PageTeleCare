````html
<h1><b>🏥 PageTeleCare 🩺</b></h1>
<a href="https://lenguajehtml.com/" target="_blank"> 
  <img src="https://img.shields.io/badge/HTML-E74C3C">
</a>
<a href="https://lenguajecss.com/" target="_blank">
  <img src="https://img.shields.io/badge/CSS-3498DB">  
</a>
<a href="https://lenguajejs.com/" target="_blank">
  <img src="https://img.shields.io/badge/JavaScript-F7DC6F">
</a>
<a href="https://www.python.org/downloads/?hl=ES" target="_blank">
  <img src="https://img.shields.io/badge/Python-52be80">
</a>
<a href="https://pypi.org/project/Flask/" target="_blank">
  <img src="https://img.shields.io/badge/Flask-707b7c">
</a>
<a href="#">
    <img src="https://img.shields.io/badge/Jinja-E74C3C">
</a>
<br><br>

<img src="https://i.pinimg.com/236x/e3/3c/2e/e33c2e7111e9b5450c5ee5b7a12b3afb.jpg">

<p>
  👩🏻‍⚕️ Esta página brinda ayuda médica a través de chatbots especializados ⚕️. Estos chatbots están 
  diseñados para ofrecer orientación sobre diversos temas de salud, respondiendo preguntas comunes y 
  ayudando a los usuarios a gestionar sus preocupaciones médicas de manera eficiente.   
</p>

---

# 🧠 TeleSalud con Inteligencia Artificial

> Plataforma web educativa que permite conocer especialidades médicas mediante chatbots con IA, incluyendo sistema de comentarios, interacción con usuarios y filtrado ético de consultas médicas.

---

## Índice de Contenidos 🧾

- Descripción 📝
- Objetivo 🎯
- Público Objetivo 👥
- Características ✨
- Arquitectura 🏗️
- Instalación 🛠️
- Uso 📘
- Despliegue en Render 🚀
- API 🔌
- Base de Datos 💾
- Seguridad ⚠️
- Uso Empresarial 🏥
- Futuras Mejoras 🔮
- Licencia 📜

---

## Descripción 📝

PageTeleCare es una plataforma web orientada al sector salud que utiliza inteligencia artificial para ofrecer orientación médica educativa mediante chatbots especializados por áreas médicas.

Incluye un sistema de interacción con usuarios, almacenamiento de comentarios y filtros de seguridad para consultas potencialmente peligrosas.

---

## Objetivo del Proyecto 🎯

- Capacitar usuarios sobre áreas médicas.
- Proporcionar orientación básica mediante IA.
- Facilitar interacción entre usuarios y contenido sanitario.
- Ofrecer una herramienta tecnológica para instituciones de salud.

---

## Público Objetivo 👥

- Pacientes
- Estudiantes de medicina
- Personal sanitario
- Empresas del sector salud
- Programadores interesados en HealthTech

---

## Características Principales ✨

- 🤖 Chatbots médicos por especialidad
- 🧠 IA integrada (modelo ML)
- 💬 Sistema de comentarios por especialidad
- 🔒 Filtro ético de emergencias médicas
- 📊 Base de datos SQLite
- 🌐 Interfaz web responsiva
- 📁 Arquitectura Flask modular

---

## Arquitectura del Sistema 🏗️

Frontend:

- HTML
- Jinja
- CSS
- JavaScript

Backend:

- Python
- Flask
- Flask-SQLAlchemy

IA:

- Modelo MLMedico

Base de datos:

- SQLite (`comentarios.db`)

---

## Estructura de Carpetas 📂

```bash
PageTeleCare/
│
├── instance/
│   └── comentarios.db
│
├── static/
│   ├── CSS/
│   ├── JS/
│   ├── IMG/
│   └── Audio/
│
├── templates/
│   ├── index.html
│   ├── Sobre_Nosotros.html
│   ├── Medicina.html
│   ├── IA.html
│   ├── Medicina_General.html
│   ├── Macros.jinja2
│   ├── Nutricion.html
│   ├── Pediatria.html
│   ├── Psicologia.html
│   ├── Cardiologia.html
│   ├── Primeros_Auxilios.html
│   ├── Ginecologia_y_Obstetricia.html
│   └── 404.html
│
├── App.py
├── Modelo_Medico.py
├── Datos_Medicos.py
└── requirements.txt
└── LICENSE
└── README.md
````

---

## Instalación 📥

Sigue estos pasos para configurar el proyecto en tu entorno local:

```bash
git clone https://github.com/Bredalis/PageTeleCare.git
cd PageTeleCare

pip install -r requirements.txt
```

Ejecutar:

```bash
python App.py
```

Abrir navegador:

```
http://127.0.0.1:5000
```

---

## Uso ⚙️

1. 📦 Haber clonado el repositorio.
2. 📝 Abrir tu editor de código o terminal.
3. 🔧 Ejecutar:

```bash
python App.py
```

4. 🌐 Abrir en navegador:

```
http://127.0.0.1:5000
```

---

## 🚀 Despliegue en Render.com

La aplicación fue desplegada utilizando la plataforma Render para permitir acceso público en la nube.

### Configuración del Servicio

Tipo de servicio:

```
Web Service
```

Build Command:

```
pip install -r requirements.txt
```

Start Command:

```
gunicorn App:app
```

La aplicación expone la variable `app` mediante:

```python
app = pagina_telecuidado()
```

---

### Base de Datos en Producción

Actualmente se utiliza SQLite:

```
instance/comentarios.db
```

⚠️ Importante:

En Render los archivos SQLite son temporales.
Para producción empresarial se recomienda PostgreSQL.

---

### Despliegue Continuo

Cada vez que se realiza un push al repositorio:

```bash
git push origin master
```

Render reconstruye automáticamente la aplicación.

---

## API Endpoints 🔌

### POST /api/teleSalud

Enviar mensaje al chatbot.

```json
{
  "mensaje": "¿Qué es la hipertensión?"
}
```

Respuesta:

```json
{
  "respuesta": "La hipertensión es..."
}
```

---

### POST /comentarios

Guardar comentarios de usuarios.

Campos:

* nombre
* comentario
* especializacion

---

## Base de Datos 💾

Tabla:

Comentario

Campos:

* id
* especializacion
* nombre
* comentario

Ubicación:

```
instance/comentarios.db
```

---

## Seguridad y Ética ⚠️

* Filtro de palabras de emergencia.
* No reemplaza atención médica profesional.
* Orientación educativa únicamente.

---

## Uso Empresarial 🏥

Posibles aplicaciones:

* Clínicas privadas
* Hospitales
* Universidades
* Plataformas de e-learning médico
* Telemedicina

---

## Futuras Mejoras 🔮

* Base de datos en la nube
* Autenticación de usuarios
* Historial de consultas
* Panel administrativo
* IA más avanzada
* Integración con APIs médicas reales

---

## Licencia 📜

Este proyecto está licenciado bajo la Licencia
GPLv3 (GNU General Public License V3.0)

---

## 👩‍💻 Autor

Desarrollado por **Bredalis Gautreaux**
Programadora Web & AI Developer

<a href="https://github.com/bredalis">GitHub</a> <a href="https://www.linkedin.com/in/bredalis-gautreaux/">LinkedIn</a>

---

## <img src="https://avatars.githubusercontent.com/u/111624948?s=400&v=4" width="50" height="50"> <img src="https://readme-typing-svg.demolab.com?font=Roboto+Slab&color=%23FFFFFF&size=35&center=true&vCenter=true&width=450&duration=1500&pause=1000&lines=Hola,+soy;Bredalis+Gautreaux!" width="auto" height="35"/>

😊 Soy una programadora con 3 años en este sector, me encanta crear y aprender constantemente. ¡Amo lo que hago! #nlp #ia 😊

## Mira mi perfil de GitHub:

[![Web](https://img.shields.io/badge/GitHub-Bredalis-14a1f0?style=for-the-badge\&logo=github\&logoColor=white\&labelColor=101010)](https://github.com/bredalis)

```