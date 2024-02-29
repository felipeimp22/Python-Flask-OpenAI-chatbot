# First configurations

## Criando e ativando o ambiente virtual

### **Windows:**
```bash
python -m venv chatbot
chatbot\Scripts\activate
```

### **Mac/Linux:**
```bash
python3 -m venv chatbot
source chatbot/bin/activate
```

---

### Instalação das bibliotecas
Caso instale sem rodar o comando: chatbot\Scripts\activate voce ira instalar fora do ambiente virtual

pip install numpy openai python-dotenv tiktoken flask opencv-python uuid

pip install -U flask-cors

---

### Ative o ambiente virtual criado do diretório .venv

chatbot\Scripts\activate

Caso já esteja utilizando o VSCode, certifique-se de que o ambiente virtual esteja selecionado como interpretador Python. Use o atalho Ctrl+Shift+P e selecione o Interpretador Python dentro do diretório bin no diretório .venv.
ou selecione um arquivo .py e no canto inferior direito valide se estara o ambiente do python exemplo versao('chatbpt':venv) exemplo2 3.12.1('chatbpt':venv)




### deploy vercerl

necessario instalar o freeze
pip install freeze

pip freeze > requirements.txt


