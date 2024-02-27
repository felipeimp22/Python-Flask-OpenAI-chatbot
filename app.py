from flask import Flask, render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

app = Flask(__name__)
app.secret_key = "myChatBot"

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    # response = bot(prompt)



@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)