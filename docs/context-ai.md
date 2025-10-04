# Simple Chat con AI

## PROMPTS
System Prompt:
Eres un experto desarrollador Python con experiencia en apps web conectadas a modelos LLM. Tu tarea es desarrollar una app siguiendo los lineamientos del archivo `context-ai.md` (estructura de carpetas, dependencias, etc). El código debe ser claro y mínimo.

User Prompt:
Siguiendo `context-ai.md`, realiza los siguientes pasos:

1. Crea un archivo `.gitignore` estándar para un proyecto Python.
2. Implementa el backend de una app de chat usando FastAPI (o Flask si se indica en el contexto).
3. El backend debe recibir mensajes de usuario y devolver la respuesta del LLM.
4. No debe haber persistencia de memoria ni almacenamiento (stateless).
5. No implementes manejo de errores ni validaciones. Código mínimo funcional.
6. Usa el modelo LLM especificado en el contexto (si es OpenAI, usar su API; si es local, simula la respuesta si hace falta).

Entrega:
- Estructura de carpetas sugerida.
- Código fuente (uno o varios archivos).


## PROGRAMACION
Programar de manera simple y clara para que un programador junior lo entienda
Explicar y comentar cada segmento del codigo
Manejar todas las claves en el backend
Programar lo maximo posible en python y lo minimo posible en Javascript
Completar lo minimo necesario del JSON para AI
Usar solo codigo Javascript que se pueda correr directamente desde navegador sin Node.js
Levantar servidor de HTML con python
Mantener el enfoque de lo ya escrito
Respetar las variables de entorno, no cambiar nunca el nombre.


## MODELOS AI
- gpt-4o
- deepseek-r1-distill-llama-8b

## VARIABLES DE ENTORNO .ENV FILE
### SERVER BACKEND
- BACKEND_HOST=
- BACKEND_PORT=
- BACKEND_PROTOCOL=
### SERVER FRONTEND
- FRONTEND_HOST=
- FRONTEND_PORT=
- FRONTEND_PROTOCOL=
### API LOCALAI 
- IA_HOST=
- IA_PROTOCOL=

## Arquitectura
API_IA: LOCALAI
Backend: Python + Flask + SQLAlchemy + Jinja2
Fronend: HTML + CSS + Javascript

## Carpetas
Proyecto
   +---app
   +---frontend
   +---docs
      +---context-ai-md



## Especificaciones API REAST AI
LOCALAI
API REST de reemplazo directo, compatible con las especificaciones de la API de OpenAI para inferencia local.

### CHAT 
-Chat Endpoint: '/v1/completions'
-Parameter content type: 'application/json'
-JSON for Chat:
{
  "backend": "string",
  "batch": 0,
  "clip_skip": 0,
  "echo": true,
  "file": "string",
  "files": [
    "string"
  ],
  "frequency_penalty": 0,
  "function_call": "string",
  "functions": [
    {
      "description": "string",
      "name": "string",
      "parameters": {
        "additionalProp1": {}
      },
      "strict": true
    }
  ],
  "grammar": "string",
  "grammar_json_functions": {
    "$defs": {
      "additionalProp1": {}
    },
    "anyOf": [
      {
        "properties": {
          "additionalProp1": {}
        },
        "type": "string"
      }
    ],
    "oneOf": [
      {
        "properties": {
          "additionalProp1": {}
        },
        "type": "string"
      }
    ]
  },
  "ignore_eos": true,
  "input": "string",
  "instruction": "string",
  "language": "string",
  "max_tokens": 0,
  "messages": [
    {
      "content": "string",
      "function_call": "string",
      "name": "string",
      "role": "string",
      "string_audios": [
        "string"
      ],
      "string_content": "string",
      "string_images": [
        "string"
      ],
      "string_videos": [
        "string"
      ],
      "tool_calls": [
        {
          "function": {
            "arguments": "string",
            "name": "string"
          },
          "id": "string",
          "index": 0,
          "type": "string"
        }
      ]
    }
  ],
  "metadata": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "mode": 0,
  "model": "string",
  "model_base_name": "string",
  "n": 0,
  "n_keep": 0,
  "negative_prompt": "string",
  "negative_prompt_scale": 0,
  "presence_penalty": 0,
  "prompt": "string",
  "quality": "string",
  "reasoning_effort": "string",
  "ref_images": [
    "string"
  ],
  "repeat_last_n": 0,
  "repeat_penalty": 0,
  "response_format": "string",
  "rope_freq_base": 0,
  "rope_freq_scale": 0,
  "seed": 0,
  "size": "string",
  "step": 0,
  "stop": "string",
  "stream": true,
  "temperature": 0,
  "tfz": 0,
  "tokenizer": "string",
  "tool_choice": "string",
  "tools": [
    {
      "function": {
        "description": "string",
        "name": "string",
        "parameters": {
          "additionalProp1": {}
        },
        "strict": true
      },
      "type": "string"
    }
  ],
  "top_k": 0,
  "top_p": 0,
  "translate": true,
  "typical_p": 0
}