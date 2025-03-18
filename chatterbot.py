import os
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Define o caminho do banco de dados SQLite
db_path = 'training_bot_db.sqlite3'
database_uri = 'sqlite:///' + db_path

# Criação do chatbot com armazenamento no banco de dados
chatbot = ChatBot(
    'TrainingBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri=database_uri
)

# Treina o chatbot somente se o banco de dados ainda não existir
if not os.path.exists(db_path):
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(
        "chatterbot.corpus.portuguese.greetings",
        "chatterbot.corpus.portuguese.conversations"
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    response = chatbot.get_response(user_input)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)
