# First configurations

## Criando e ativando o ambiente virtual

### **Windows:**
```bash
python -m venv chatbot
chatbot\Scripts\activate
or
python -m venv venv
venv\Scripts\activate

venv\scripts\activate


```

### **Mac/Linux:**
```bash
python3 -m venv chatbot
source chatbot/bin/activate

or
source venv/bin/activate

```

---

### Instalação das bibliotecas
Caso instale sem rodar o comando: chatbot\Scripts\activate voce ira instalar fora do ambiente virtual

pip install numpy openai python-dotenv tiktoken flask opencv-python uuid

pip install -U flask-cors

pip install numpy openai python-dotenv tiktoken flask opencv-python uuid flask-cors

ou installe tudo com :
pip install -r requirements.txt

---

### Ative o ambiente virtual criado do diretório .venv

chatbot\Scripts\activate

Caso já esteja utilizando o VSCode, certifique-se de que o ambiente virtual esteja selecionado como interpretador Python. Use o atalho Ctrl+Shift+P e selecione o Interpretador Python dentro do diretório bin no diretório .venv.
ou selecione um arquivo .py e no canto inferior direito valide se estara o ambiente do python exemplo versao('chatbpt':venv) exemplo2 3.12.1('chatbpt':venv)




### deploy vercerl

necessario instalar o freeze
pip install freeze

pip freeze > requirements.txt

npm i -g vercel
vercel
or
vercel --prod


