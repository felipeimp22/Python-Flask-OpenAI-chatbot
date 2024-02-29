from flask import Flask, render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
from time import sleep
from flask_cors import CORS
from helpers import *
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

app = Flask(__name__)
app.secret_key = "myChatBot"
CORS(app)

contexto = carrega("dados/globo.txt")

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            prompt_do_sistema = f"""
            Você é um chatbot de atendimento a clientes da empresa Globo. 
            Você não deve responder perguntas que não sejam dados do globo informado!
            você deve gerar resposostas utilizando o contexto abaixo.
            # Contexto
            {contexto}
            """
            response = cliente.chat.completions.create(
                messages=[
                        {
                                "role": "system",
                                "content": prompt_do_sistema
                        },
                        {
                                "role": "user",
                                "content": prompt
                        }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                model = modelo)
            return response
        except Exception as erro:
                repeticao += 1
                if repeticao >= maximo_tentativas:
                        return "Erro no GPT: %s" % erro
                print('Erro de comunicação com OpenAI:', erro)
                sleep(1)


@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    print("*********************************************.", resposta)
    text_response = resposta.choices[0].message.content
    return text_response

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # app.run(debug = True)
    app.run(host="0.0.0.0", port=os.getenv("PORT", 5000))
    