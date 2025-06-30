# app.py
import gradio as gr
import requests

AGENT_URL = "https://p4z3ag25yfyhasncve24sapj.agents.do-ai.run"

def preguntar_ia(pregunta):
    try:
        r = requests.post(AGENT_URL, json={"input": pregunta})
        return r.json().get("output", "No se recibió respuesta.")
    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(
    fn=preguntar_ia,
    inputs="text",
    outputs="text",
    title="🤖 Asistente de Matemáticas",
    description="Haz preguntas como: ¿cómo dividir? ¿cómo derivar x^2? ¿quieres un test?",
)

demo.launch()
