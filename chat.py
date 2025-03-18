import webbrowser
import os
import signal
from threading import Timer
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulação de respostas do chatbot
responses = {
    "oi": "Olá! Como posso te ajudar?",
    "como você está?": "Estou bem, obrigado por perguntar!",
    "qual seu nome?": "Sou um chatbot de Engenharia de Software.",
    "adeus": "Até mais! Foi bom conversar com você."
}

# Função para abrir o navegador automaticamente
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Rota para processar mensagens do usuário
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").lower()
    response = responses.get(user_message, "Desculpe, não entendi. Pode reformular?")
    return jsonify({"response": response})

# Endpoint para fechar o servidor Flask
@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)  # Encerra o processo do Flask
    return "Servidor encerrado."

if __name__ == "__main__":
    Timer(1, open_browser).start()  # Abre o navegador automaticamente
    app.run(debug=True)