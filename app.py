import gradio as gr
import requests

# ✅ Este es el endpoint correcto para tu agente GenAI
AGENT_ID = "1b809e51-553f-11f0-bf8f-4e013e2ddde4"
API_URL = f"https://genai-api.cloud.digitalocean.com/v1/agents/{AGENT_ID}/invoke"

# ✅ Clave del Endpoint Access Key (trátala como confidencial)
API_TOKEN = "IXf15HI24hJSYWxI_7ng32H95VEbFkf8"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def preguntar_ia(pregunta):
    try:
        response = requests.post(API_URL, json={"input": pregunta}, headers=headers)
        return response.json().get("output", "No se recibió respuesta.")
    except Exception as e:
        return f"❌ Error: {e}"

demo = gr.Interface(
    fn=preguntar_ia,
    inputs="text",
    outputs="text",
    title="🤖 Asistente de Matemáticas",
    description="Haz preguntas como: ¿cómo dividir?, ¿cómo derivar x²?, o pídele un test.",
)

# 👇 Esto es clave para que funcione en App Platform (puerto 8080)
demo.launch(server_name="0.0.0.0", server_port=8080)
