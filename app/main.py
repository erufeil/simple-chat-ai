# Importación de librerías necesarias
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación Flask y habilitar CORS para peticiones del frontend
app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Configurar la URL del endpoint de LocalAI usando variables de entorno
LOCAL_AI_URL = f"{os.getenv('IA_PROTOCOL')}://{os.getenv('IA_HOST')}/v1/completions"

# Ruta principal que sirve el archivo index.html
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Endpoint para procesar mensajes del chat
@app.route('/chat', methods=['POST'])
def chat():
    # Obtener el mensaje enviado por el usuario desde el request
    data = request.json
    
    # Preparar el payload para LocalAI siguiendo su formato específico
    payload = {
        "model": "deepseek-r1-distill-llama-8b",  # Modelo especificado en el contexto
        "messages": [{"role": "user", "content": data['message']}],
        "temperature": 0.7  # Control de creatividad en las respuestas
    }

    # Enviar la petición a LocalAI y obtener la respuesta
    response = requests.post(LOCAL_AI_URL, json=payload)
    ai_response = response.json()
    
    # Devolver solo el contenido de la respuesta al frontend
    return jsonify({"response": ai_response['choices'][0]['message']['content']})

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    app.run(
        host=os.getenv('BACKEND_HOST'),
        port=int(os.getenv('BACKEND_PORT'))
    )
