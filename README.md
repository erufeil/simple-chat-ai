# Simple Chat AI

Una aplicación de chat minimalista que utiliza Flask como backend y LocalAI como motor de procesamiento de lenguaje natural.

## Requisitos Previos

- Python 3.8 o superior
- LocalAI configurado y ejecutándose
- Navegador web moderno

## Estructura del Proyecto

```
simple-chat-ai/
├── app/
│   ├── __init__.py
│   └── main.py
├── frontend/
│   ├── index.html
│   └── chat.js
├── .env
├── .gitignore
└── requirements.txt
```

## Configuración del Entorno

1. Clonar el repositorio:
```bash
git clone <url-repositorio>
cd simple-chat-ai
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Unix o MacOS:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crear un archivo `.env` en la raíz del proyecto con:
```
BACKEND_HOST=localhost
BACKEND_PORT=5000
BACKEND_PROTOCOL=http

FRONTEND_HOST=localhost
FRONTEND_PORT=5000
FRONTEND_PROTOCOL=http

IA_HOST=localhost
IA_PROTOCOL=http
```

## Ejecución del Servidor

1. Asegurarse de que LocalAI esté en ejecución

2. Iniciar el servidor Flask:
```bash
python app/main.py
```

3. Acceder a la aplicación:
Abrir el navegador y visitar: `http://localhost:5000`

## Testing Manual

1. Enviar un mensaje de prueba:
   - Abrir la aplicación en el navegador
   - Escribir un mensaje en el campo de texto
   - Hacer clic en "Send"
   - Verificar que se recibe una respuesta del modelo

2. Testing con curl:
```bash
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"Hola, ¿cómo estás?"}'
```

## Notas Técnicas

- La aplicación es stateless (sin estado)
- Utiliza el modelo deepseek-r1-distill-llama-8b de LocalAI
- No implementa manejo de errores para mantener el código minimal
- CORS está habilitado para permitir peticiones desde el frontend
