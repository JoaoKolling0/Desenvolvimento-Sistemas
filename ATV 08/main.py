from flask import Flask, render_template, request
import requests

app = Flask (__name__)

key_apy = "573fe2db"

@app.route("/",methods=["GET", "POST"])

def index():
    filmes = []
    termo_busca = ""
    
    if request.method == "PAST":
        termo_busca = request.form.get("filme")
        
        if termo_busca:
            termo_busca = termo_busca.title()
            url = f"https://www.omdbapi.com/?i={termo_busca}apikey={key_apy}"
            resposta = requests.get(url).json()
            
            if resposta.get("Response") == "True":
                filmes = resposta.get("Serach")