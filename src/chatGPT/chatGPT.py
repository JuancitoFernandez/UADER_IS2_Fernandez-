import os
import readline  # Para historial y flecha ↑
from openai import OpenAI
import json

# Cliente de OpenAI con tu API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Historial de consultas
historial = []

def obtener_consulta():
    """
    Solicita una consulta al usuario. Si presiona ↑ recupera la última consulta.
    """
    try:
        consulta = input("Ingrese su consulta (↑ para reutilizar): ").strip()
        if not consulta and historial:
            consulta = historial[-1]
            print(f"(Reutilizando): {consulta}")
        return consulta
    except Exception as e:
        print(f"Error al leer la consulta: {e}")
        return None

def preparar_mensaje(consulta):
    """
    Prepara los mensajes para enviar a la API.
    """
    try:
        mensaje_usuario = f"You: {consulta}"
        mensajes = [
            {"role": "system", "content": "Eres un asistente útil que responde en español."},
            {"role": "user", "content": mensaje_usuario}
        ]
        return mensajes
    except Exception as e:
        print(f"Error al preparar los mensajes: {e}")
        return None

def invocar_chatgpt(mensajes):
    """
    Invoca la API de ChatGPT y devuelve la respuesta formateada.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            response_format={"type": "json_object"},
            messages=mensajes,
            temperature=1,
            max_tokens=2048
        )
        contenido = response.choices[0].message.content
        return f"chatGPT: {contenido}"
    except Exception as e:
        print(f"Error al invocar la API de ChatGPT: {e}")
        return None

def main():
    """
    Función principal que coordina la ejecución del programa.
    """
    print("=== Consulta a ChatGPT ===")
    while True:
        consulta = obtener_consulta()
        if not consulta:
            print("Consulta vacía. Intente nuevamente.")
            continue

        print(f"You: {consulta}")
        historial.append(consulta)

        mensajes = preparar_mensaje(consulta)
        if not mensajes:
            continue

        respuesta = invocar_chatgpt(mensajes)
        if respuesta:
            print(respuesta)

        seguir = input("\n¿Desea hacer otra consulta? (s/n): ").lower()
        if seguir != "s":
            break

if __name__ == "__main__":
    main()
