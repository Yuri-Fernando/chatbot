import os
from flask import Flask, render_template, request, jsonify
import openai
import requests
import dialogflow_v2 as dialogflow  # Certifique-se de instalar: pip install google-cloud-dialogflow

app = Flask(__name__)

# --- Configurações de API ---

# OpenAI (GPT)
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

# Dialogflow (Google IA)
DIALOGFLOW_PROJECT_ID = "YOUR_DIALOGFLOW_PROJECT_ID"
DIALOGFLOW_LANGUAGE_CODE = "pt-BR"
SESSION_ID = "current-session-id"

# Alexa (Endpoint simulado – substitua pelo seu endpoint real)
ALEXA_ENDPOINT = "https://api.example.com/alexa"  # Exemplo; altere para o endpoint real
ALEXA_API_KEY = "YOUR_ALEXA_API_KEY"

# --- Funções para chamar as APIs ---

def get_response_gpt(input_text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro na API GPT: {str(e)}"

def get_response_google(input_text):
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(text=input_text, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
    except Exception as e:
        return f"Erro na API Google: {str(e)}"

def get_response_alexa(input_text):
    try:
        payload = {"query": input_text}
        headers = {"Authorization": f"Bearer {ALEXA_API_KEY}"}
        response = requests.post(ALEXA_ENDPOINT, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("response", "Sem resposta da Alexa")
        else:
            return f"Erro na API Alexa: {response.status_code}"
    except Exception as e:
        return f"Erro na API Alexa: {str(e)}"

# --- Rota de interação ---

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get("msg")
    service = request.args.get("service", "gpt").lower()  # Default para GPT
    if service == "gpt":
        response_text = get_response_gpt(user_input)
    elif service == "google":
        response_text = get_response_google(user_input)
    elif service == "alexa":
        response_text = get_response_alexa(user_input)
    else:
        response_text = "Serviço não reconhecido. Use 'gpt', 'google' ou 'alexa'."
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
